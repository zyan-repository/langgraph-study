# LangGraph Study —— 简体中文指南

[English Guide](README.en.md)

## 概览
LangGraph Study 是跟随 Vaibhav Mehra freeCodeCamp 课程的动手实验集，官方参考仓库位于 [LangGraph-Course-freeCodeCamp](https://github.com/iamvaibhavmehra/LangGraph-Course-freeCodeCamp/)。点击这里查看 [YouTube 教程](https://www.youtube.com/watch?v=jGg_1h0qzaM)。

## 项目结构
```
langgraph-study/
├── tutorials/
│   ├── materials/          # 教程读取的 PDF/Dataset 素材
│   └── …                   # 课程 Notebook 与脚本
├── docs/
│   ├── README.en.md        # 英文文档
│   └── README.zh.md        # 中文文档
├── README.md
└── requirements.txt
```

## 教学大纲（tutorials/01-10）
- `01-hello-world.ipynb` —— 聚焦最小 `StateGraph` 的编译与单节点执行验证。
- `02-multiple-inputs.ipynb` —— 演示带类型的状态结构与由输入驱动的算术分支。
- `03-sequential-agent.ipynb` —— 说明顺序节点如何传递累积状态，打造线性流程。
- `04-conditional-agent.ipynb` —— 通过 `graph.add_conditional_edges` 进行加减法路由切换。
- `05-looping.ipynb` —— 构建循环与终止条件，展示 LangGraph 处理迭代式流程的方式。
- `06-agent-bot.py` —— 结合 `ChatGoogleGenerativeAI`，实现 Gemini 加持的 CLI 聊天代理。
- `07-memory-agent.py` —— 维护多轮对话记忆并在结束后将聊天记录写入日志文件。
- `08-ReAct.py` —— 构建带工具调用的 ReAct 代理，可按需选择加减乘等算术工具。
- `09-Drafter.py` —— 文档撰写代理，利用 update/save 工具流式更新内容并保存成文本。
- `10-rag-agent.py` —— 读取 PDF、建立 Chroma 向量库的 RAG 代理，用检索工具回答 2024 股市问题并引用来源。

## 教程素材
所有教程需要读取的 PDF、数据集或其他辅助内容，统一放在 `tutorials/materials/` 文件夹，方便 Notebook 之间复用并保持相对路径一致。

## 快速启动
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
