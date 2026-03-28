# 🤖 AI Capstone Project — Research & Document Assistant

## 🚀 Overview

This project is an end-to-end AI application that combines:

- Large Language Models (LLMs)
- Retrieval Augmented Generation (RAG)
- External tool integration
- API deployment using FastAPI

The system can:
- Answer questions from documents (PDF)
- Use external knowledge (tool)
- Generate structured AI responses
- Serve responses via API

---

## 🧠 Architecture

User Request → FastAPI API → AI Pipeline  
                 ↓  
           RAG (PDF Retrieval)  
           Tool (External Info)  
              ↓  
            LLM → Final Answer  

---

## ⚙️ Features

- 📄 Document ingestion (PDF)
- ✂️ Text chunking
- 🔍 Vector search using FAISS
- 🧠 Embeddings with Sentence Transformers
- 🛠️ Tool integration (external knowledge)
- 🌐 FastAPI deployment
- 🔁 Fallback mode (works without API key)

---

## 📁 Project Structure
ai-capstone/
│
├── main.py # FastAPI server
├── ai_pipeline.py # Core AI logic
├── rag.py # Embeddings + retrieval
├── loader.py # PDF loader + chunking
├── tools.py # External tool
├── .env # API keys
│
└── documents/


---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-capstone.git
cd ai-capstone

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install fastapi uvicorn requests python-dotenv sentence-transformers faiss-cpu pypdf

🔐 Environment Variables

Create a .env file:

LLM_API_KEY=your_api_key
LLM_API_URL=https://api.openai.com/v1/chat/completions
LLM_MODEL=gpt-4o-mini

⚠️ If not provided, the app runs in fallback mode.

▶️ Run the Application
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000/docs
