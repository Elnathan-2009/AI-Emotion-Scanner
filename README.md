# AI Emotion Scanner

A real-time facial emotion detection system built with Python, OpenCV, DeepFace, and TensorFlow.

## Overview

This project uses a webcam to detect faces and analyze facial expressions in real time.

The system can:

- Detect faces through a webcam
- Detect multiple faces
- Draw bounding boxes around detected faces
- Classify facial emotions
- Display detected emotions in real time
- Determine whether a person is present
- Provide a simple emotion-based focus estimate

## Technologies

- Python 3.10
- OpenCV
- DeepFace
- TensorFlow

## How It Works

1. The webcam captures a video frame.
2. OpenCV processes the frame.
3. DeepFace analyzes detected faces.
4. The system identifies the dominant facial emotion.
5. The detected emotion is displayed on the video feed.
6. A simple focus estimate is generated from the detected emotion.

## Installation

Install the required packages:

```bash
pip install -r requirements.txt