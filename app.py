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

    with mp_pose.Pose(
        static_image_mode=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # BGR → RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Mediapipe Pose detect
            results = pose.process(image)

            # Draw skeleton
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS
                )

            # Display in Streamlit
            stframe.image(image, channels="RGB")

    cap.release()
