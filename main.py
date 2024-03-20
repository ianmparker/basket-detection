from ultralytics import YOLO
if __name__ == "__main__":
    
    # 1) Run this file i.e. main.py
    # 2) Go to runs/detect/train/weights and use best.pt as the model while running shot_detector.py
    
    # Load a model
    model = YOLO('Yolo-Weights/yolov8n.pt')

    # Train the model. Each epoch is a iteration of the model scanning the entire dataset. We will do this 100 times to improve confidence. 
    results = model.train(data='config.yaml', epochs=100, imgsz=640)
