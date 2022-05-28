import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image

def app():

    st.header("THE EXPLORATORY DATA ANALYSIS !")
    image2 = Image.open('car_eda4.jpg')
    st.image(image2)
    st.write("""
    *Image Source: [Pinterest](https://in.pinterest.com/pin/310748443050907590/)*
    """)

    st.write("""
    ##### Want to do Data Analysis for some other dataset? Well then here you go!
    """)

    st.write("""
    In this Data Analysis application user can either use the dataset provided on the Microsoft Engage website([cars_engage_2022](https://raw.githubusercontent.com/AvanthyYeluri/Data-Analysis-App/main/cars_engage_2022.csv))by clicking on the button below or can upload a CSV file from their device.
    """)

    ## Upload CSV data
    with st.sidebar.header("Upload your CSV data"):
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
        st.sidebar.markdown("""
        [Microsoft Engage dataset (cars_engage_2022.csv)](https://raw.githubusercontent.com/AvanthyYeluri/Data-Analysis-App/main/cars_engage_2022.csv)
        """)

    #Pandas Profiling Report
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv
        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Data Analysis Report**')
        st_profile_report(pr)
    else:
        st.info("Waiting for the CSV file to be uploaded...")
        if st.button('Press to use Microsoft Engage Dataset (cars_engage_2022.csv)'):
            # Example data
            @st.cache
            def load_data():
                url = "https://raw.githubusercontent.com/AvanthyYeluri/Data-Analysis-App/main/cars_engage_2022.csv"
                a = pd.read_csv(url, sep=',')
                return a
            df = load_data()
            pr = ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Data Analysis Report**')
            st_profile_report(pr)
