import streamlit as st
from PIL import Image
import mediapipe as mp
import tempfile
import cv2

st.title("Mediapipe Pose Skeleton Demo")
st.write("Upload a video to extract skeleton and view frames.")

uploaded = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded:
    # Save uploaded file temporarily
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(uploaded.read())

    # Mediapipe setup
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    stframe = st.empty()   # Video output placeholder

    cap = cv2.VideoCapture(temp.name)

