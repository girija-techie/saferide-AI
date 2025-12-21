import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),  # postgres or saferide_db
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

def get_recent_detections(limit=10):
    cur = conn.cursor()
    cur.execute("""
        SELECT created_at, class_id, confidence, s3_url
        FROM detections
        ORDER BY created_at DESC
        LIMIT %s
    """, (limit,))
    rows = cur.fetchall()
    cur.close()
    return rows

def count_by_class(class_id):
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*)
        FROM detections
        WHERE class_id = %s
    """, (class_id,))

    count = cur.fetchone()[0]
    cur.close()
    return count

def get_summary_stats():
    cur = conn.cursor()
    cur.execute("""
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN class_id = 2 THEN 1 ELSE 0 END) AS accidents,
            SUM(CASE WHEN class_id = 1 THEN 1 ELSE 0 END) AS no_helmet,
            ROUND(AVG(confidence)::numeric, 2) AS avg_confidence
        FROM detections
    """)
    
    stats = cur.fetchone()
    cur.close()
    return {
        "total": stats[0],
        "accidents": stats[1],
        "no_helmet": stats[2],
        "avg_confidence": float(stats[3]) if stats[3] is not None else 0.0
    }
