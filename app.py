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
