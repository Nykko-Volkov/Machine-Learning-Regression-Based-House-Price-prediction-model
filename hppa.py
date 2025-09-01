import streamlit as st
import joblib



size = st.slider('Enter the size of the house in square feet', 500, 5000, 1000)
st.write('Size of the house:', size, 'square feet')
model = joblib.load('house_price_model.pkl')
price = model.predict([[size]])
st.write('The estimated price of the house is $', price[0])

