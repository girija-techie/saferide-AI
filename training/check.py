from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")
    model.train(
        data="dataset.yaml",
        epochs=1,
        device=0,
        workers=0   # extra safety
    )

if __name__ == "__main__":
    main()
