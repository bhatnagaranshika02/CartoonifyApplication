import streamlit as st 
from PIL import Image
from cartoon import image

st.title("Upload your image")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")

    st.write("Cartoonifying")
    label=image(uploaded_file)
    image1 = Image.open(lable)
    st.image1(Label, caption='Cartoonify Image.', use_column_width=True)
    
        

