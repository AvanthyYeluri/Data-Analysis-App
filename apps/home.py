import streamlit as st
from PIL import Image

def app():
    st.header('DATA ANALYSIS')
    image1 = Image.open("car_home.jpg")
    st.image(image1)
    st.write("""
    *Image Source*: [Pinterest](https://in.pinterest.com/pin/43347215154725593/)""")

    st.write("""
    This application demonstrates how Automobile Industry can use the data set provided to decide upon popular car specifications like engine type, fuel etc.. and predicting the Selling Prcie of the car so that the user can take informed decisions!
    """)

    st.write("""
    So! why wait let's go and delve deep into the world of exploration!!!
    """)

    
