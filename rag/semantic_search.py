from rag.embeddings import embed
from rag.vector_store import vector_db

def semantic_search(query, k=3):
    results = vector_db.search(embed(query), k)

    if not results:
        return ["No semantic matches found yet."]

    return results
