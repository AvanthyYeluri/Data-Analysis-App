import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def app():
    sns.set_style("darkgrid")

    st.header('EXPLORATORY DATA ANALYSIS')

    image2 = Image.open('car_eda1.jpg')
    st.image(image2)
    st.write("""
    *Image Source: [Pinterest](https://in.pinterest.com/pin/347621664996292031/)*
    """)
    st.write("""
    ### Buying a Car?
    """)
    st.write("""
    Want to know how exactly different factors like ***Number of Kilometers*** driven by the car, ***Fuel Type*** of the car, ***Gear Transmission*** of the car... affect the price of the car you want to buy or maybe the features in a car that might be most common so that you can buy a car that can stand out!
    """)
    st.write("""
    ##### Well than you are at the right place!
    """)
    st.write("""
    Now! why late let's hop on and explore the data to see how different features in a car can influence the Selling Price of the car and also how a particular feature can be preferred over another!!!

    The dataset taken here for Exploratory Data Analysis is the [Vehicle Dataset](https://github.com/AvanthyYeluri/Data-Analysis-App/blob/main/car%20data.csv) by CarDekho.com which has also been used to predict the Selling Price of the cars.
    """)

    #Data Overview
    st.write("""
    ##### **Let's have a look into the Data that we have considered for analysis**
    """)
    df = pd.read_csv('car data.csv')
    st.write(df)

    #UNIVARIATE ANALYSIS
    if st.button('UNIVARIATE ANALYSIS'):
        st.subheader('UNIVARIATE ANALYSIS')

        #Fuel_Type
        st.write("""
        ##### Type of the Fuel used in cars
        """)
        fig = px.histogram(df, x='Fuel_Type', color_discrete_sequence=['cadetblue'] )
        st.plotly_chart(fig)
        st.write("""
        It's evident that most of the cars run on petrol! This might primarily be because Petrol cars come cheaper as they are manufactured at a lower cost when compared to Diesel cars which deliver better fuel efficiency and command a better price in the resale market.
        """)

        #Seller Type
        st.write("""
        ##### Type of Sellers in the market
        """)
        fig = px.histogram(df, x='Seller_Type', color_discrete_sequence=['cadetblue'] )
        st.plotly_chart(fig)
        st.write("""
        Dealers are quite a lot in the market as compared to Individuals!
        """)

        #Transmission
        st.write("""
        ##### Transmission of the car
        """)
        fig = px.histogram(df, x='Transmission', color_discrete_sequence=['cadetblue'] )
        st.plotly_chart(fig)
        st.write("""
        Most of the cars have Manual transmission as compared to Automatic as they have better fuel efficiency, less complex engine, weigh less and have more gears than automatics! Whereas Automatic transmissions are more expensive, easier to use and more comfortable for the driver
        """)

        #Owner
        st.write("""
        ##### Past Owners
        """)
        fig = px.histogram(df, x='Owner', color_discrete_sequence=['cadetblue'] )
        st.plotly_chart(fig)
        st.write("""
        Looks like most of the cars in the Automobile Market are at Owner 0!
        """)

        #Kms Driven
        st.write("""
        ##### Number of Kilometers travelled by the car
        """)
        fig = px.box(df, y='Kms_Driven', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)
        st.write("""
        From the box plot it is advisable to consider a car that has travelled less than 50,000 kilometers and obviously it needs to be in good condition too!
        """)

        #Age of the Car
        st.write("""
        ##### Age of the cars
        Taking into account that the current year is 2022 the age of the car has been calculatedand that will be considered a feature rather than the given column *Year*
        """)
        df['Age'] = 2022-df['Year']
        fig = px.box(df, y='Age', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)
        st.write("""
        Most of the cars in the market have their age in between 6 to 10 years and it is also advisable to buy a car of age in this range as this minimizes depreciation and maximises reliability for the price you'll pay
        """)

        #Present Price
        st.write("""
        ##### Present Price of the car in lakhs
        """)
        fig = px.box(df, y='Present_Price', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)
        st.write("""
        Present Price of the car is something of importance that needs to be kept in mind while deciding upon the Selling Price of the car in the market
        """)

        #Selling Price
        st.write("""
        ##### Selling Price of the car in lakhs
        (Also our target variable here!)
        """)
        fig = px.box(df, y='Selling_Price', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)

    if st.button('BIVARIATE ANALYSIS'):
        st.subheader('BIVARIATE ANALYSIS')

        #Age vs Selling Price
        st.write("""
        ##### Age of the car VS Selling Price of the car
        Age of the car is calculated considering the current year to be 2022
        """)
        df['Age'] = 2022-df['Year']
        fig = px.scatter(df, x = 'Age', y = 'Selling_Price', trendline = 'ols', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)
        st.write("""
        The selling price is decreasing for ageing vehicles!
        """)

        #Present Price vs Selling Price
        st.write("""
        ##### Present Price VS Selling Price of the cars
        Both Present Price and Selling Price of the car are in lakhs
        """)
        fig = px.scatter(df, x = 'Present_Price', y = 'Selling_Price', trendline = 'ols', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)
        st.write("""
        Selling Price tends to increse gradually with an increase in Present Price of the vehicle!
        """)

        #Kms Driven vs Selling Price
        st.write("""
        ##### Distance travelled by the car VS Selling Price
        """)
        fig = px.scatter(df, x = 'Kms_Driven', y = 'Selling_Price', trendline = 'ols', color_discrete_sequence=['cadetblue'])
        st.plotly_chart(fig)
        st.write("""
        The selling price is found to be higher for vehicles with less kilometers covered!
        """)

        #Fuel Type vs Selling Price
        st.write("""
        ##### Fuel type of the car VS Selling Price
        """)
        fig = plt.figure(figsize=(10, 4))
        sns.barplot(x='Fuel_Type', y='Selling_Price', data=df, palette="Blues_d")
        st.pyplot(fig)
        st.write("""
        Diesel Engine Vehicles are found to have the highest selling price amongst Petrol and CNG engine vehicles!
        """)

        #Seller Type vs Selling Price
        st.write("""
        ##### Seller Type VS Selling Price
        """)
        fig = plt.figure(figsize=(10, 4))
        sns.barplot(x='Seller_Type', y='Selling_Price', data=df, palette="Blues_d")
        st.pyplot(fig)
        st.write("""
        Dealers can sell vehicles at a higher selling price than a general individual. No surprises though!
        """)

        #Transmission vs Sellin Price
        st.write("""
        ##### Transmission of the car VS Selling Price
        """)
        fig = plt.figure(figsize=(10, 4))
        sns.barplot(x='Transmission', y='Selling_Price', data=df, palette="Blues_d")
        st.pyplot(fig)
        st.write("""
        Automatic vehicles are found to have a large resale value in the market compared to Manual transmission!
        """)

        #Owner vs Selling Price
        st.write("""
        ##### Owner VS Selling Price
        """)
        fig = plt.figure(figsize=(10, 4))
        sns.barplot(x='Owner', y='Selling_Price', data=df, palette="Blues_d")
        st.pyplot(fig)
        st.write("""
        The vehicles belonging to Owner 0 have the highest selling price!
        """)

    st.write("""
    ### Any data analysis feels incomplete without a Heatmap and Pairplot showing the correlations among the features, so let's take a dive into it!
    """)
    if st.button("HEATMAP AND PAIRPLOT"):
        st.write("""
        Before plotting Heatmap and Pairplot we will be performing feature engineering on the dataset for a better correlation which includes
        * Dropping the 'Year' column as the 'Age' column is now added and is being taken into account
        * Dropping the 'Car_Name' column  because it only has text info that the model can't use!
        * Encoding Categorical columns
        """)
        df['Age'] = 2022-df['Year']
        df.drop('Year', axis=1, inplace=True)
        df.drop('Car_Name', axis=1, inplace=True)
        df=pd.get_dummies(data=df,columns=['Fuel_Type', 'Transmission', 'Seller_Type'], drop_first=True)

        #Heatmap
        st.write("""
        #### HEATMAP
        """)
        correlations=df.corr()
        indx=correlations.index
        plt.figure(figsize=(26,22))
        sns.heatmap(df[indx].corr(),annot=True,cmap="YlGnBu")
        st.pyplot()

        #Pairplot
        st.write("""
        #### PAIRPLOT
        """)
        fig = sns.pairplot(df)
        st.pyplot(fig)
        st.write("""
        ###### Selling price seems to be considerably correlated with the Present Price feature!
        """)
    st.set_option('deprecation.showPyplotGlobalUse', False)
