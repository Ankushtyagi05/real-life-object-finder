# Object Finder 🔍

A real-time object detection tool powered by **YOLOv5** and **OpenCV**. Detect objects in static images or live through your webcam — all with a simple command-line interface.

---

## Features

- **Image Detection** — Run object detection on any local image file
- **Real-Time Webcam Detection** — Live object detection through your webcam feed
- **YOLOv5s Model** — Uses a lightweight, pre-trained YOLOv5 small model for fast inference
- **Cross-Platform** — Works on Windows, macOS, and Linux

---

## Requirements

- Python 3.8+
- A webcam (for real-time detection mode)

### Dependencies

Install all required packages via pip:



> YOLOv5 will be loaded automatically via `torch.hub` on first run — an internet connection is required for the initial download.

---

## Usage

Run the script from your terminal:

```bash
python objectfinder.py
```

You will be prompted to choose a mode:

```
Choose an option:
1. Detect objects in an image
2. Real-time object detection from webcam
Enter 1 or 2:
```

### Option 1 — Image Detection

Enter the path to a local image file when prompted:

```
Enter image path: /path/to/your/image.jpg
```

A window will open displaying the image with detected objects highlighted by bounding boxes and labels.

### Option 2 — Webcam Detection

The webcam feed will open in a new window with live bounding boxes drawn around detected objects.

Press **`Q`** to quit the webcam stream.

---

## How It Works

The project uses the [YOLOv5](https://github.com/ultralytics/yolov5) model (You Only Look Once), a state-of-the-art, real-time object detection architecture. The `yolov5s` (small) variant is used here for a good balance between speed and accuracy.

- **Image mode** — The image is read with OpenCV, passed to the model, and results are rendered in a pop-up window.
- **Webcam mode** — Frames are captured in a loop, processed by the model, and displayed in real time. Results are converted from RGB to BGR for correct OpenCV rendering.

-
