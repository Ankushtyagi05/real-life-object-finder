import torch
import cv2
import numpy as np
import pathlib
import platform

# Fix for pathlib issue on Windows when loading YOLOv5 cache
if platform.system() == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath

# Load the pre-trained YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)


def detect_objects(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image at '{image_path}'. Please check the path.")
        return
        
    results = model(image)
    results.show()  # Display detected objects

def detect_from_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Failed to read frame from webcam.")
            break

        results = model(frame)

        # Convert results to OpenCV format. YOLOv5 render returns RGB, convert to BGR
        rendered_img = cv2.cvtColor(np.array(results.render()[0]), cv2.COLOR_RGB2BGR)
        cv2.imshow("Real-Time Object Detection", rendered_img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Choose mode
print("Choose an option:\n1. Detect objects in an image\n2. Real-time object detection from webcam")
choice = input("Enter 1 or 2: ")

if choice == "1":
    image_path = input("Enter image path: ")
    detect_objects(image_path)
elif choice == "2":
    detect_from_webcam()
else:
    print("Invalid choice. Exiting.")