import requests
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_accident_alert(confidence, image_url):
    ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))
    caption = f"""
🚨 ACCIDENT DETECTED!

🕒 Time: {ist_time.strftime('%Y-%m-%d %H:%M:%S')}
📊 Confidence: {confidence:.2f}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    payload = {
        "chat_id": CHAT_ID,
        "photo": image_url,   # 🔥 THIS IS THE KEY
        "caption": caption
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()
