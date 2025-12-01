import streamlit as st
import cv2


st.title('Hello, kitty')
st.write('this is for deplying at streamlit')


img = cv2.imread("lena.png")

st.image(img)
