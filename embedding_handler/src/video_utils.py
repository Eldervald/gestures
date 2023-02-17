import cv2
import numpy as np


def read_video(filepath: str) -> np.array:
    cap = cv2.VideoCapture(filepath)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

    return np.stack(frames)
