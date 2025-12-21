import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import uuid
import time
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from cloud.s3_utils import upload_image
from cloud.rds_utils import log_detection
from alerts.telegram_alert import send_accident_alert
from cloud.s3_utils import generate_presigned_url
from rag.chat_logic import answer_question
from rag.ingest_vectors import ingest_detection_logs


if "vectors_loaded" not in st.session_state:
    ingest_detection_logs()
    st.session_state.vectors_loaded = True


if "inference_done" not in st.session_state:
    st.session_state.inference_done = False

if "last_image_id" not in st.session_state:
    st.session_state.last_image_id = None


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="SafeRide AI – Helmet & Accident Detection",
    layout="wide"
)

st.title("🛵 SafeRide AI – Helmet & Accident Detection")
st.markdown("Detect **Helmet / No Helmet / Accident** from images or videos")

# -----------------------------
# Load YOLO Model (cached)
# -----------------------------
@st.cache_resource
def load_model():
    return YOLO("training/helmet_accident_detection/clean_restart_v1/weights/best.pt")

model = load_model()

# -----------------------------
# Confidence Threshold
# -----------------------------
conf_threshold = st.slider(
    "Confidence Threshold",
    min_value=0.1,
    max_value=1.0,
    value=0.4,
    step=0.05
)

# -----------------------------
# Mode Selection
# -----------------------------
# mode = st.radio(
#     "Choose Input Type",
#     ["Image", "Video"]
# )
mode = "Image"
# ======================================================
# IMAGE INFERENCE
# ======================================================
if mode == "Image":

    uploaded_image = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:

        # Unique ID for uploaded image
        image_id = uploaded_image.name + str(uploaded_image.size)

        # Run inference ONLY if this is a NEW image
        if st.session_state.last_image_id != image_id:
            st.session_state.inference_done = False
            st.session_state.last_image_id = image_id

        if not st.session_state.inference_done:

            left_col, right_col = st.columns([1, 1])

            with left_col:
                image = Image.open(uploaded_image).convert("RGB")
                image_np = np.array(image)

                st.subheader("Original Image")
                st.image(image, use_container_width=True)

            with right_col:
                with st.spinner("Running image detection..."):
                    results = model(image_np, conf=conf_threshold)

                annotated_image = results[0].plot()
                st.subheader("Detection Result")
                st.image(annotated_image, use_container_width=True)




            # Save temp image
            temp_filename = f"results/temp_{uuid.uuid4().hex}.jpg"
            cv2.imwrite(temp_filename, annotated_image)

            class_names = ["helmet", "no_helmet", "accident"]

            for box in results[0].boxes:
                class_id = int(box.cls[0])
                class_name = class_names[class_id]
                conf = float(box.conf[0])

                s3_key, s3_url = upload_image(temp_filename, class_name)

                if class_name == "accident" and conf > 0.4:
                    presigned_url = generate_presigned_url(s3_key)
                    send_accident_alert(conf, presigned_url)

                log_detection(
                    class_id=class_id,
                    confidence=conf,
                    bbox=box.xyxy[0].tolist(),
                    s3_url=s3_url
                )

            st.session_state.inference_done = True

            # Detection Summary
            st.subheader("Detection Summary")
            names = results[0].names
            boxes = results[0].boxes

            if boxes is not None:
                for box in boxes:
                    cls_id = int(box.cls[0])
                    conf = float(box.conf[0])
                    st.write(f"• **{names[cls_id]}** → Confidence: `{conf:.2f}`")
        else:
            st.info("Inference already completed for this image.")

st.divider()
st.header("🤖 SafeRide AI – Detection Chatbot")

with st.form(key="chat_form", clear_on_submit=True):
    user_question = st.text_input(
        "Ask about detections:",
        placeholder="e.g. How many accidents today?"
    )
    submit = st.form_submit_button("Ask")

if submit and user_question:
    answer = answer_question(user_question)
    st.html(body=answer)




# ======================================================
# VIDEO INFERENCE
# ======================================================


# elif mode == "Video":

#     uploaded_video = st.file_uploader(
#         "Upload a Video",
#         type=["mp4", "avi", "mov"]
#     )

#     if uploaded_video is not None:

#         # Save input video
#         os.makedirs("outputs/videos", exist_ok=True)
#         input_path = os.path.join("outputs/videos", uploaded_video.name)

#         with open(input_path, "wb") as f:
#             f.write(uploaded_video.read())

#         st.subheader("Original Video")
#         st.video(input_path)

#         # Output video path
#         output_path = os.path.join(
#             "outputs/videos",
#             f"output_{uploaded_video.name}"
#         )

#         cap = cv2.VideoCapture(input_path)

#         width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         fps = cap.get(cv2.CAP_PROP_FPS)

#         if fps == 0:  # safety fallback
#             fps = 25

#         fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#         out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

#         frame_count = 0
#         total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#         progress = st.progress(0)

#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             results = model(frame, conf=conf_threshold)
#             annotated = results[0].plot()
#             out.write(annotated)

#             frame_count += 1
#             if total_frames > 0:
#                 progress.progress(frame_count / total_frames)

#         cap.release()
#         out.release()

#         st.success("✅ Video processing completed!")

#         # PLAY VIDEO
#         st.subheader("Processed Video")
#         st.video(output_path)

#         # DOWNLOAD BUTTON
#         with open(output_path, "rb") as f:
#             st.download_button(
#                 label="⬇️ Download Processed Video",
#                 data=f,
#                 file_name=os.path.basename(output_path),
#                 mime="video/mp4"
#             )
