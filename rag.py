from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    return model.encode(chunks)


def build_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index


def retrieve(query, chunks, index, k=3):
    query_vec = model.encode([query])
    _, indices = index.search(query_vec, k)
    return [chunks[i] for i in indices[0]]