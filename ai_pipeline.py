import os
import requests
from dotenv import load_dotenv

from loader import load_pdf, chunk_text
from rag import create_embeddings, build_index, retrieve
from tools import search_tool

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
API_URL = os.getenv("LLM_API_URL")
MODEL = os.getenv("LLM_MODEL")


# ✅ Load RAG once
if os.path.exists("documents/knowledge.pdf"):
    text = load_pdf("documents/knowledge.pdf")
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    index = build_index(embeddings)
else:
    chunks = []
    index = None


def call_llm(prompt):

    # ✅ fallback (no API needed)
    if not API_KEY:
        return f"""
[No API Mode]

Based on context:

{prompt[:500]}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    if "choices" not in data:
        return str(data)

    return data["choices"][0]["message"]["content"]


def ai_pipeline(question):

    # 🔹 RAG retrieval
    if index:
        context_docs = retrieve(question, chunks, index)
        context = "\n".join(context_docs)
    else:
        context = "No document available"

    # 🔹 Tool usage
    tool_output = search_tool(question)

    prompt = f"""
You are an AI assistant.

Context:
{context}

Tool Data:
{tool_output}

Question:
{question}

Answer clearly and professionally.
"""

    return call_llm(prompt)