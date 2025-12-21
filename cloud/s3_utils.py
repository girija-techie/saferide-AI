import boto3
import os
from datetime import datetime
from botocore.config import Config
from dotenv import load_dotenv

# FORCE load .env from project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))


s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION"),
    config=Config(signature_version="s3v4")
)
BUCKET = os.getenv("S3_BUCKET_NAME")

def upload_image(local_path, class_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(local_path)

    s3_key = f"detections/{class_name}/{timestamp}_{filename}"

    s3.upload_file(local_path, BUCKET, s3_key)

    return s3_key, f"s3://{BUCKET}/{s3_key}"

def generate_presigned_url(s3_key, expires=3600):
    print("s3_key", s3_key)
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": s3_key},
        ExpiresIn=expires
    )