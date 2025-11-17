import streamlit as st
import time
from PIL import Image
import os 

st.title("ML Model at the SERVER!!")

st.header("Intro")
st.subheader("This is the subheader")

st.text("This is text")

input_text = st.text_input("Type", "some text")
st.text(input_text)

input_text = st.text_area("Enter Here", "tjhis is a large ")

button = st.button("Click Me")
if button:
    print(f"Current working directory: {os.getcwd()}")
    img = Image.open("tiger.jpeg")
    st.image(img)


selection = st.radio("Select One", ["NLP", "Audio"])
st.write(selection)

selection = st.multiselect("Select Any", ["NLP", "Audio", "Text"])
st.write(selection)

with st.spinner("Downloading ... please wait"):
    st.write("download your model here")
    time.sleep(10)