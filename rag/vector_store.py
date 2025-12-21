import faiss
import numpy as np

DIM = 1536
index = faiss.IndexFlatL2(DIM)
documents = []

class VectorDB:
    def add(self, text, embedding):
        documents.append(text)
        index.add(np.array([embedding]).astype("float32"))

    def search(self, embedding, k=3):
        if len(documents) == 0:
            return []   # 🔥 PREVENT INDEX ERROR

        k = min(k, len(documents))
        D, I = index.search(np.array([embedding]).astype("float32"), k)
        return [documents[i] for i in I[0] if i < len(documents)]

vector_db = VectorDB()
