import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import matplotlib.pyplot as plt

def app():

    st.write("""
    # CAR PRICE PREDICTION
    """)

    image2 = Image.open('car_model1.jpg')
    st.image(image2)
    st.write("""
    *Image Source: [Pinterest](https://in.pinterest.com/pin/481744491395840737/)*
    """)

    st.write("""
    #### Here we predicts the ***Selling Price*** of Cars.

    We get data from the car website CarDekho.com, filled with information on a wide variety of cars, including their selling price and present price. We realize that we can use this data to make sure we get a good deal on a new car. In particular, we can figure out exactly how much one should pay for a specific type of car.

    Data obtained from Kaggle [Vehicle Dataset](https://github.com/AvanthyYeluri/Data-Analysis-App/blob/main/car%20data.csv) by CarDekho
    """)

    #Collecting User Input Features
    st.sidebar.header('User Input Parameters')
    def user_input_features():
        Present_Price = st.sidebar.number_input('Present Price in Lakhs', min_value=0.00, value=5.00)
        Kms_Driven = st.sidebar.number_input('Number of Kilometers driven by the car', value=10000)
        Fuel_Type = st.sidebar.selectbox('Fuel Type', ('Petrol', 'Diesel', 'CNG'))
        Seller_Type = st.sidebar.selectbox('Seller Type', ('Dealer', 'Individual'))
        Transmission = st.sidebar.selectbox('Car Transmission', ('Manual', 'Automatic'))
        Owner = st.sidebar.slider('Number of persons who owned the car before(Past Owners)', 0, 50, 0, 1)
        Year = st.sidebar.number_input('Year in which the car was brought', min_value=2000, max_value=2022, step=1, value=2011)
        data = {'Year': Year,
                'Present_Price': Present_Price,
                'Kms_Driven': Kms_Driven,
                'Fuel_Type': Fuel_Type,
                'Seller_Type': Seller_Type,
                'Transmission': Transmission,
                'Owner': Owner}
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    #Combining the user input features with entire car datasets
    #This will be useful for encoding and feature engineering phase
    car_df_raw = pd.read_csv('car data.csv')
    car_df = car_df_raw.drop(columns = ['Selling_Price', 'Car_Name'])
    df = pd.concat([input_df, car_df], axis=0)

    #Selects only the first row (the user input data)
    #df = df[:1]

    #Displays the user input features
    st.subheader('User Input Features')
    st.write(df[:1])
    st.write("""
    Now, since we have got the User Input Parameters we can jump onto the prediction of the Selling Price of the Car based on the input parameters given!
    """)

    #Feature Engineering
    df['Age'] = 2022-df['Year']
    df.drop('Year', axis=1, inplace=True)

    #Encoding Categorical Columns
    df=pd.get_dummies(data=df,columns=['Fuel_Type', 'Transmission', 'Seller_Type'], drop_first=True)

    #Selects only the first row (the user input data)
    df = df[:1]

    # Reads in saved classification model
    load_model = pickle.load(open('carprice_regressor_model.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_model.predict(df)

    st.subheader('Predicted Selling Price of the car in lakhs is:')
    st.write(prediction)

    st.info("We have used Gradient Boosting Regression(XGBRegressor) model as it was performing considerably better to predict the Selling Price of the car and this had an R2 score of 0.96571")
    st.write("""
    Well this might be the maximum amount that can be invested on the car given it is perfectly alright. But the minimum has no bounds well because sometimes it all comes down to how tactfully you market it too!
    """)

    st.write("""
    ##### Also
    """)

    st.info("Diesel engines are more powerful than Petrol fuelled engines and hence good fuel efficiency. However Petrol cars give good initial power so for short distances a Petrol car will make more sense.")

    st.info("Automatic Transmissions are easy to drive and does not require too much of driver input which is reverse in case of Manual Transmission. But Manual Transmissions on the other hand are more relaible than Automatic Transmission and also have low maintainence cost.")

    st.info("When buying a pre-owned car it is better to go for a car that travelled less than 10,000-15,000 kilometers per year and as a general rule it is better to avoid cars that have travelled more than 300,000 kilometers unless it has been maintained well or the price is tempting.")

    st.info("Purchasing a car that is just 2-3 years old can sometimes be a better investment as it is a massive saving compared to a new car and it is itself a kind off new car too!")

    st.write("""
    ##### In reality, it all depends on the car. A well-maintained 10-year-old car could possibly be a better investment than a newer model which hasn't been looked after.

    ##### So, it is better if the user takes these things into account as well so that all his needs are addressed and decide upon the Selling Price!!!
    """)
