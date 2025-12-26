# 🚦 SafeRide AI  
### Intelligent Road Safety Monitoring System  

**AI-powered real-time detection of helmet violations and road accidents with cloud deployment, instant alerts, and intelligent analytics.**

---

![Python](https://img.shields.io/badge/Python-3.12.7-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3%20%7C%20RDS-orange?logo=amazon-aws)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![FAISS](https://img.shields.io/badge/RAG-FAISS-purple)

---

SafeRide AI is an **end-to-end, production-ready road safety monitoring system** that automatically detects **helmet violations** and **road accidents** using deep learning and cloud services.

It integrates:
- **Real-time YOLOv8-based detection**
- **Secure cloud storage (AWS S3 & RDS)**
- **Instant Telegram alerts**
- **Agent-based RAG chatbot for analytics and reporting**

to enable **faster accident response**, **automated enforcement**, and **data-driven road safety insights**.


## 🔍 Problem Statement

Manual traffic monitoring systems are inefficient, error-prone, and slow in responding to accidents and violations. There is a strong need for an **automated, intelligent, and scalable solution** that can:

- Detect helmet violations in real time  
- Identify road accidents instantly  
- Alert authorities without delay  
- Store evidence securely  
- Provide analytics and reports on demand  

---

## 🎯 Solution Overview

SafeRide AI addresses these challenges by combining:

- **YOLOv8 deep learning models** for real-time detection  
- **AWS cloud services** for scalable storage and logging  
- **Telegram alerts** for instant accident notifications  
- **Agent-based RAG chatbot** for querying detection logs  
- **Automated HTML & email reports** with analytics  

---

## ✨ Key Features

- 🧠 **YOLOv8-based Detection**
  - Helmet
  - No Helmet
  - Road Accident

- 🖼️ **Image Inference Pipeline**

- ☁️ **AWS Cloud Integration**
  - S3 → Evidence storage
  - RDS (PostgreSQL) → Detection logs
  - EC2 → Deployment

- 🚨 **Real-Time Telegram Alerts**
  - Triggered on accident detection
  - Includes confidence & secure image link

- 🤖 **Agent-Based RAG Chatbot**
  - SQL-based queries
  - Semantic search using FAISS
  - Report & email triggering

- 📊 **Automated Reporting**
  - HTML reports
  - Summary statistics
  - Charts & visual analytics
  - Secure S3 links

- 🔐 **Secure Credential Management**
  - Environment variables only
  - No hardcoded secrets

---

## 🏗️ System Architecture

```
Image Input
       ↓
YOLOv8 Inference Engine
       ↓
Detection Results
       ↓
+------------------------------+
| AWS S3 | AWS RDS |
| Evidence| Metadata Logs |
+------------------------------+
       ↓
Telegram Accident Alerts
       ↓
RAG Chatbot (SQL + Vector)
       ↓
Reports / Email / Analytics
```

---

## 🧠 Technology Stack

### AI & ML
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- FAISS (Vector Search)

### Backend & Cloud
- Python
- AWS EC2
- AWS S3
- AWS RDS (PostgreSQL)

### Frontend
- Streamlit

### Notifications & Reports
- Telegram Bot API
- Gmail SMTP (App Password)
- HTML Reports
- Matplotlib Charts

---

## 📂 Project Structure

```
SafeRide-AI/
├── app/
│ └── streamlit_app.py
├── cloud/
│ ├── s3_utils.py
│ ├── rds_utils.py
├── alerts/
│ └── telegram_alert.py
├── rag/
│ ├── embeddings.py
│ ├── vector_store.py
│ ├── semantic_search.py
│ ├── db_queries.py
│ ├── report_tool.py
│ ├── email_tool.py
│ └── chat_logic.py
├── models/
│ └── best.pt
├── training/
│ └── helmet_accident_detection/
├── requirements.txt
├── README.md
└── .env (ignored)
```

---

## 🧪 Model Training Summary

- Model: **YOLOv8**
- Epochs: **60**
- Image Size: **640 × 640**
- Batch Size: **4**
- Datasets:
  - Helmet / No Helmet dataset
  - Road Accident dataset (Roboflow)

### Evaluation Metrics
- Precision
- Recall
- mAP@0.5
- mAP@0.5:0.95

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/yourusername/SafeRide-AI.git
cd SafeRide-AI
```

### 2️⃣ Create Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a .env file (do not commit):

``` bash
AWS_ACCESS_KEY_ID=xxxx
AWS_SECRET_ACCESS_KEY=xxxx
AWS_REGION=eu-north-1

DB_HOST=xxxx.rds.amazonaws.com
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=xxxx

TELEGRAM_BOT_TOKEN=xxxx
TELEGRAM_CHAT_ID=xxxx

EMAIL_USER=your_email@gmail.com
EMAIL_APP_PASSWORD=xxxx
ADMIN_EMAIL=your_email@gmail.com
```

### ▶️ Run the Application

``` bash
streamlit run app/streamlit_app.py
```

## 🤖 RAG Chatbot Capabilities

The chatbot supports:

- **Structured Queries**
  - “How many accidents today?”

- **Semantic Queries**
  - “Show risky incidents”

- **Reports**
  - “Generate report”

- **Email Delivery**
  - “Send email report”

All responses are **grounded in real detection data** (no hallucinations).

---

## ☁️ Deployment (AWS EC2)

- Ubuntu 22.04 LTS
- Streamlit served on port **8501**
- YOLO model loaded locally (`best.pt`)
- Secrets managed via environment variables
- Logging enabled using system services

---

## 🔐 Security Practices

- No credentials in source code
- Environment variables only
- Private S3 bucket with pre-signed URLs
- SSH key-based EC2 access
- Restricted security groups

---

## 📈 Results & Impact

- Real-time detection and alerts
- Faster accident response
- Automated enforcement support
- Centralized evidence storage
- Intelligent analytics via chatbot

---

## 🚀 Future Enhancements

- GPU-based inference
- Live CCTV stream processing
- License plate recognition
- Web dashboard for authorities
- Mobile application
- Predictive accident analytics

---

## 🎓 Academic Context

This project was developed as a **final-year / capstone project**, demonstrating:

- Applied deep learning
- Cloud-native deployment
- Intelligent agent-based systems
- End-to-end AI product design

---

## 📜 License

This project is intended for **academic and educational use**.

---

## 🙌 Acknowledgements

- Ultralytics YOLOv8
- AWS Cloud Services
- PostgreSQL
- Telegram Bot API
- FAISS




