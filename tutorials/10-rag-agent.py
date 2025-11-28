import os
import operator
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

pdf_path = "materials/Stock_Market_Performance_2024.pdf"

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF file not found at path: {pdf_path}")

pdf_loader = PyPDFLoader(pdf_path)

try:
    pages = pdf_loader.load()
    print(f"Loaded {len(pages)} pages from the PDF.")
except Exception as e:
    print(f"An error occurred while loading the PDF: {e}")
    raise

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

pages_split = text_splitter.split_documents(pages)

persist_directory = "./output"
collection_name = "stock_market"

if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

try:
    vector_store = Chroma.from_documents(
        documents=pages_split,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name
    )
    print(f"Created ChromaDB vector store with collection '{collection_name}'.")
except Exception as e:
    print(f"Error setting up ChromaDB: {e}")
    raise

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

@tool
def retrieve_tool(query: str) -> str:
    """
    This tool searches and returns the information from the Stock Market Performance 2024 document.
    """

    docs = retriever.invoke(query)

    if not docs:
        return "I found no relevant information in the Stock Market Performance 2024 document."
    
    results = []
    for i, doc in enumerate(docs):
        results.append(f"Document {i+1}:\n{doc.page_content}\n")
    
    return "\n\n".join(results)

tools = [retrieve_tool]

llm = llm.bind_tools(tools)

class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage], operator.add]

system_prompt = """
You are an intelligent AI assistant who answers questions about stock market performance in 2024 based on the provided document.
Use the 'retrieve_tool' to fetch relevant information from the document when needed.
If you need to look up some information before asking a follow up question, you are allowed to use the 'retrieve_tool'.
Please always cite the specific parts of the document you used to formulate your answers.
"""

tools_dict = {our_tool.name: our_tool for our_tool in tools}

def call_llm(state: AgentState) -> AgentState:
    messages = [SystemMessage(content=system_prompt)] + list(state["messages"])
    
    response = llm.invoke(messages)
    
    return {"messages": [response]}

# Retriever Agent
def take_action(state: AgentState) -> AgentState:
    tool_calls = state["messages"][-1].tool_calls
    results = []
    for t in tool_calls:
        print(f"Calling Tool: {t['name']} with query: {t['args'].get('query', 'No query provided')}")

        if not t['name'] in tools_dict:
            print(f"Tool {t['name']} not found.")
            result = "Incorrect Tool Name, Please Retry and Select tool from list of Available Tools."
        else:
            result = tools_dict[t['name']].invoke(t['args'].get('query', ''))
            print(f"Result length: {len(str(result))}")
        
        results.append(ToolMessage(tool_call_id=t['id'], name=t['name'], content=str(result)))
    
    print("Tool Execution Completed. Back to the model!")
    return {"messages": results}

graph = StateGraph(AgentState)
graph.add_node("llm", call_llm)
graph.add_node("retriever_agent", take_action)

graph.add_edge(START, "llm")
graph.add_conditional_edges(
    "llm",
    tools_condition,
    {
        "tools": "retriever_agent",
        END: END
    }
)
graph.add_edge("retriever_agent", "llm")

rag_agent = graph.compile()

def running_agent():
    print("\n=== RAG AGENT ===")

    while True:
        user_input = input("\nWhat is your question: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages = [HumanMessage(content=user_input)]

        result = rag_agent.invoke({"messages": messages})

        print("\n=== AGENT RESPONSE ===")
        
        last_message = result["messages"][-1]
        content = last_message.content
        
        if isinstance(content, list):
            full_text = "".join([part.get("text", "") for part in content if "text" in part])
            print(full_text)
        else:
            print(content)

running_agent()