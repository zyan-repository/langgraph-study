import operator
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv

load_dotenv()

DB = {"document_content": ""}

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

@tool
def update(content: str) -> str:
    """Update the document with new content."""
    DB["document_content"] = content
    return f"Document updated. Current content:\n{content}"

@tool
def save(filename: str) -> str:
    """Save the document to a file."""
    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        with open(filename, "w") as file:
            file.write(DB["document_content"])
        return f"Document saved to {filename}."
    except Exception as e:
        return f"Failed to save: {e}"

tools = [update, save]

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind_tools(tools)

def our_agent(state: AgentState) -> AgentState:
    current_doc = DB["document_content"]
    
    system_prompt = SystemMessage(content=f"""
        You are Drafter. 
        Current Document Content:
        ---
        {current_doc}
        ---
        If user wants to update, use 'update' tool.
        If user wants to save, use 'save' tool.
    """)
    
    messages = [system_prompt] + list(state["messages"])
    
    response = model.invoke(messages)
    
    return {"messages": [response]}

graph = StateGraph(AgentState)
graph.add_node("agent", our_agent)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "agent")

# - If the Agent returns tool_calls -> Automatically routes to the "tools" node.
# - If the Agent did not call a tool -> Automatically routes to END.
graph.add_conditional_edges("agent", tools_condition)

graph.add_edge("tools", "agent")

app = graph.compile()

def run_document_agent():
    print("\n--- Drafter Document Agent ---\n")
    
    chat_history = []
    
    print("AI: I'm ready. What would you like to do?")

    while True:
        try:
            user_input = input("\nUser: ")
            if user_input.lower() == "quit": 
                break
        except EOFError:
            break
        
        # 1. Add user message to chat history
        user_msg = HumanMessage(content=user_input)
        chat_history.append(user_msg)
        
        # Construct input State
        inputs = {"messages": chat_history}

        # Run the graph with streaming
        for step in app.stream(inputs, stream_mode="updates"):
            for node, values in step.items():
                if "messages" in values:
                    new_msgs = values["messages"]
                    # Synchronize new messages back to chat history
                    chat_history.extend(new_msgs)
                    
                    for msg in new_msgs:
                        # --- Printing logic ---
                        if isinstance(msg, AIMessage):
                            content = msg.content
                            # Handle Gemini list format
                            if isinstance(content, list) and len(content) > 0:
                                content = content[0].get("text", "")
                            
                            if content and str(content).strip():
                                print(f"🤖 AI: {content}")
                            
                            if msg.tool_calls:
                                tool_names = [t['name'] for t in msg.tool_calls]
                                print(f"🛠️ USING TOOLS: {tool_names}")

                        elif isinstance(msg, ToolMessage):
                            print(f"✅ Tool Result: {msg.content}")
                            
                            # 4. Detect exit condition here 
                            if "saved to" in msg.content:
                                print("\n--- Document Saved. Exiting... ---")
                                return

if __name__ == "__main__":
    run_document_agent()