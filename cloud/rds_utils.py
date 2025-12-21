import psycopg2
import os
import json
from dotenv import load_dotenv

# FORCE load .env from project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def get_connection():
    print("DEBUG RDS_HOST:", os.getenv("DB_HOST"))  # TEMP DEBUG

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def log_detection(class_id, confidence, bbox, s3_url):
    conn = get_connection()
    cur = conn.cursor()

    bbox_json = json.dumps(bbox)

    cur.execute("""
        INSERT INTO detections (class_id, confidence, bbox, s3_url)
        VALUES (%s, %s, %s, %s)
    """, (class_id, confidence, bbox_json, s3_url))

    conn.commit()
    cur.close()
    conn.close()
