import mediapipe as mp
import cv2
import numpy as np
from PIL import Image
import random

def detect_pose(pil_img):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True)
    img = np.array(pil_img)
    results = pose.process(img)
    if results.pose_landmarks:
        return results.pose_landmarks.landmark
    return []

def evaluate_fit(landmarks):
    if not landmarks:
        return "Could not detect full body. Please upload a full-body image."

    shoulder_width = abs(landmarks[11].x - landmarks[12].x)
    hip_width = abs(landmarks[23].x - landmarks[24].x)
    ratio = shoulder_width / (hip_width + 1e-6)

    if ratio > 1.2:
        return "Your top appears more prominent. Consider balancing with flared pants."
    elif ratio < 0.8:
        return "Lower body seems wider. Try a tailored top or layering."
    else:
        return "Nice proportion! Your outfit looks well balanced."

def classify_style(image):
    # Dummy classifier - replace with real model later
    styles = ["Streetwear", "Casual", "Formal", "Athleisure", "Boho"]
    return random.choice(styles)
