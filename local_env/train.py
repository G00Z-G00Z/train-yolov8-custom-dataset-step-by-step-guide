from ultralytics import YOLO

last_best_train_run_no: int = 27
EPOCHS: int = 100
# Load a model
model = YOLO(
    f"../runs/detect/train{last_best_train_run_no}/weights/best.pt"
)  # build a new model from scratch

# Use the model
results = model.train(
    data="config.yaml",
    epochs=EPOCHS,
    amp=False,
)  # train the model
