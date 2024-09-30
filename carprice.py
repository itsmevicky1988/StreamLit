import streamlit as st

import yfinance as yf
import datetime
import pickle
import pandas as pd

cars_df = pd.read_csv('./car_price.csv')
st.write(
    '''
    # Cars 24 Price Data
    '''
)

st.dataframe(cars_df.head())
col1, col2 =st.columns(2)
fuel_type = col1.selectbox("select the car fuel",['Diesel', 'Petrol', 'Electrical', 'CNG'])
engine = col1.slider('select the engine power', 500, 5000, step=100)
transmission = col2.selectbox('select the transmission type',('Manual', 'Automatic'))
seats = col2.selectbox('select the nos of seats', [4, 5, 7, 9, 11])

#feature = (2018, 1, 4000, fuel_type, transmission, 14.5, engine, 85, seats)
#features should write in the same sequence as given in datasheet
encode_dict={
    "fuel_type": {'Diesel':1, 'Petrol':2, 'Electrical':3, 'CNG':4},
    "transmission" : {'Manual':1, 'Automatic':2}
}

def model_pred(fuel_type, engine, transmission, seats):
    #loading the model

    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)
        feature = [[2018, 1, 4000, fuel_type, transmission, 14.5, engine, 85, seats]]
        return reg_model.predict(feature)
if st.button('Predict_price'):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission = encode_dict['transmission'][transmission]

    price = model_pred(fuel_type, transmission, engine, seats)
    st.text(f"The price of the car is {price[0].round(2)} lakh rupees")