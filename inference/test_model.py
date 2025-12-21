from ultralytics import YOLO

model = YOLO("training/helmet_accident_detection/clean_restart_v1/weights/best.pt")

results = model("data/processed/final/images/test", conf=0.4)

results[0].show()
