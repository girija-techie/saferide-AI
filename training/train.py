from ultralytics import YOLO
import multiprocessing

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="dataset.yaml",
        epochs=60,
        imgsz=640,
        batch=4,          # keep small for GTX 1650
        lr0=0.0015,
        lrf=0.01,
        device=0,
        workers=0,
        amp=False,
        cache=False,
        freeze=0,
        project="helmet_accident_detection",
        name="clean_restart_v1",
        patience=30
    )

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
