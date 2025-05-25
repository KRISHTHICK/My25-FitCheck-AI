# My25-FitCheck-AI
GenAI

Here’s a fresh **fashion AI project** idea that **does not require virtual environments** and works directly in **VS Code** and **GitHub**:

---

## 👟 **Project Name: FitCheck AI – Outfit Fit & Style Feedback**

### 🧠 Overview:

**FitCheck AI** is an app where users upload their full-body outfit photos, and the AI gives:

* Feedback on the **fit (tight/loose/proportional)**.
* Suggestions to **improve the silhouette or style**.
* Classifies the **style** (e.g., casual, streetwear, formal).

---

## 🎯 Features:

* 📸 Upload full-body outfit image.
* 🤖 Pose detection to evaluate fit.
* 📏 Suggest if the outfit is too tight, oversized, or balanced.
* 🧥 Classify into style categories using a simple CNN.
* 📝 Get improvement tips (e.g., “Try slimmer pants”, “Layering suggestion”).

---

## 📂 Folder Structure:

```
FitCheck-AI/
├── app.py
├── model/
│   └── style_classifier.pkl  (dummy model)
├── utils.py
├── test_images/
│   └── example1.jpg
├── requirements.txt
└── README.md
```

---

## 📄 `requirements.txt`

```txt
streamlit
opencv-python
mediapipe
scikit-learn
Pillow
```

---

## 🧾 `app.py`

```python
import streamlit as st
from PIL import Image
import numpy as np
from utils import detect_pose, evaluate_fit, classify_style

st.set_page_config(page_title="FitCheck AI", layout="centered")
st.title("👟 FitCheck AI – Outfit Fit & Style Feedback")

uploaded_file = st.file_uploader("Upload your full-body outfit photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Outfit", use_column_width=True)

    st.subheader("👁️ Analyzing Fit & Style...")

    keypoints = detect_pose(image)
    fit_feedback = evaluate_fit(keypoints)
    style_label = classify_style(image)

    st.markdown(f"### 📏 Fit Analysis:\n{fit_feedback}")
    st.markdown(f"### 🧥 Style Classification:\n**{style_label}**")

    st.success("Done! Want to try another?")
```

---

## 🧠 `utils.py`

```python
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
```

---

## 🚀 How to Run

```bash
# Install dependencies (no venv needed)
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📝 `README.md`

````markdown
# 👟 FitCheck AI – Outfit Fit & Style Feedback

## 💡 About
FitCheck AI is a fashion assistant that gives feedback on your outfit fit and style based on pose detection and visual features.

## 🚀 Features
- Upload your full-body outfit photo
- Get feedback on how well your outfit fits
- Style classification (streetwear, formal, etc.)
- Style improvement suggestions

## 🧰 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
````

## ❗ Note

This project uses MediaPipe for pose estimation and simulates style classification. You can later plug in a trained CNN model.

```

---

Would you like me to:
- Add PDF download with feedback?
- Include a trained style classifier model?
- Generate a ZIP file or GitHub-ready version?
```
