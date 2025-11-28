# LangGraph Study — English Guide

[简体中文指南](README.zh.md)

## Overview
LangGraph Study is a “clone & learn” mini-lab for following Vaibhav Mehra’s freeCodeCamp LangGraph course—sponsored by Scrimba—with the official reference repo here: [LangGraph-Course-freeCodeCamp](https://github.com/iamvaibhavmehra/LangGraph-Course-freeCodeCamp/). [YouTube tutorial](https://www.youtube.com/watch?v=jGg_1h0qzaM)

## Directory Layout
```
langgraph-study/
├── tutorials/
│   ├── materials/          # PDFs and other assets consumed by tutorials
│   └── …                   # Lesson notebooks and scripts
├── docs/
│   ├── README.en.md        # English documentation
│   └── README.zh.md        # Chinese documentation
├── README.md
└── requirements.txt
```

## Teaching Outline (tutorials/01-10)
- `01-hello-world.ipynb` – Focus on defining a minimal `StateGraph`, compiling it, and verifying single-node execution flow.
- `02-multiple-inputs.ipynb` – Demonstrates typed state schemas and branching arithmetic logic driven by structured inputs.
- `03-sequential-agent.ipynb` – Shows how to stitch multiple nodes linearly while passing accumulated state between stages.
- `04-conditional-agent.ipynb` – Highlights conditional routing with `graph.add_conditional_edges` for add/sub pipelines.
- `05-looping.ipynb` – Implements loopbacks and halting conditions to model iterative workflows (guessing game pattern).
- `06-agent-bot.py` – Integrates `ChatGoogleGenerativeAI` with LangGraph to build a Gemini-backed CLI chat loop.
- `07-memory-agent.py` – Maintains conversation history for iterative chats and logs transcripts to disk.
- `08-ReAct.py` – Builds a tool-using ReAct agent that chooses arithmetic tools dynamically.
- `09-Drafter.py` – Drafts documents via update/save tools, streaming responses until the file is persisted.
- `10-rag-agent.py` – Implements a PDF-backed RAG agent using Chroma + Gemini embeddings for cited answers.

## Tutorial Assets
Place any PDFs, datasets, or other supporting assets that lessons need to read under `tutorials/materials/`. Keeping shared material together there keeps relative imports stable across notebooks.

## Quick Start
### macOS / Linux
```bash
cd /Users/zyan/study/langgraph-study
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name langgraph-study
jupyter lab --notebook-dir=tutorials
```

### Windows PowerShell
```powershell
cd /Users/zyan/study/langgraph-study
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab --notebook-dir=tutorials
```
