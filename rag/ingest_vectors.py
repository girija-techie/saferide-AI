from rag.db_queries import get_recent_detections
from rag.embeddings import embed
from rag.vector_store import vector_db

def ingest_detection_logs(limit=100):
    rows = get_recent_detections(limit)

    for r in rows:
        text = f"{r[1]} detected at {r[0]} with confidence {r[2]}\n"
        embedding = embed(text)
        vector_db.add(text, embedding)
