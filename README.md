# LangGraph Study

[English](#english) | [简体中文](#简体中文)

## English

### Overview
LangGraph Study is a “clone & learn” mini-lab for following Vaibhav Mehra’s freeCodeCamp LangGraph course—sponsored by Scrimba—with the official reference repo here: [LangGraph-Course-freeCodeCamp](https://github.com/iamvaibhavmehra/LangGraph-Course-freeCodeCamp/). Lessons `01`–`05` mirror the video exercises, and `06` recreates the Gemini-powered CLI bot so you can validate your implementation against the source walkthrough. [YouTube tutorial](https://www.youtube.com/watch?v=jGg_1h0qzaM)

### Directory Layout
```
langgraph-study/
├── tutorials/              # All notebooks and scripts for the lessons
├── README.md
└── requirements.txt
```

### Teaching Outline (tutorials/01-06)
- `01-hello-world.ipynb` – Focus on defining a minimal `StateGraph`, compiling it, and verifying single-node execution flow.
- `02-multiple-inputs.ipynb` – Demonstrates typed state schemas and branching arithmetic logic driven by structured inputs.
- `03-sequential-agent.ipynb` – Shows how to stitch multiple nodes linearly while passing accumulated state between stages.
- `04-conditional-agent.ipynb` – Highlights conditional routing with `graph.add_conditional_edges` for add/sub pipelines.
- `05-looping.ipynb` – Implements loopbacks and halting conditions to model iterative workflows (guessing game pattern).
- `06-agent-bot.py` – Integrates `ChatGoogleGenerativeAI` with LangGraph to build a Gemini-backed CLI chat loop.

### Quick Start
#### macOS / Linux
```bash
cd /Users/zyan/study/langgraph-study
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name langgraph-study
jupyter lab --notebook-dir=tutorials
```

#### Windows PowerShell
```powershell
cd /Users/zyan/study/langgraph-study
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab --notebook-dir=tutorials
```

All lessons assume resources live one directory up (for example `../data` if you add datasets later), so relative imports remain tidy.

---

## 简体中文

### 概览
LangGraph Study 是跟随 Vaibhav Mehra freeCodeCamp 课程的动手实验集，官方参考仓库位于 [LangGraph-Course-freeCodeCamp](https://github.com/iamvaibhavmehra/LangGraph-Course-freeCodeCamp/)。`01`–`05` 对应视频中的练习代理，`06` 复刻 Gemini CLI Bot，便于对照官方实现。[YouTube 教程](https://www.youtube.com/watch?v=jGg_1h0qzaM)

### 项目结构
```
langgraph-study/
├── tutorials/              # 全部 Notebook 与脚本
├── README.md
└── requirements.txt
```

### 教学大纲（tutorials/01-06）
- `01-hello-world.ipynb` —— 聚焦最小 `StateGraph` 的编译与单节点执行验证。
- `02-multiple-inputs.ipynb` —— 演示带类型的状态结构与由输入驱动的算术分支。
- `03-sequential-agent.ipynb` —— 说明顺序节点如何传递累积状态，打造线性流程。
- `04-conditional-agent.ipynb` —— 利用 `graph.add_conditional_edges` 进行加减法路由切换。
- `05-looping.ipynb` —— 构建循环与终止条件，展示 LangGraph 处理迭代式流程的方式。
- `06-agent-bot.py` —— 结合 `ChatGoogleGenerativeAI`，实现 Gemini 加持的 CLI 聊天代理。

### 快速启动
#### macOS / Linux
```bash
cd /Users/zyan/study/langgraph-study
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name langgraph-study
jupyter lab --notebook-dir=tutorials
```

#### Windows PowerShell
```powershell
cd /Users/zyan/study/langgraph-study
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab --notebook-dir=tutorials
```

