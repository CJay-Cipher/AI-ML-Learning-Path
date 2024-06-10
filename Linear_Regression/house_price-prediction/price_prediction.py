import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the input features
input_features = ['bedrooms', 'bathrooms', 'toilets', 'parking_space', 'title', 'town', 'state']

# Load the unique values for title and town
unique_titles = ['Detached Duplex', 'Semi Detached Duplex', 'Terraced Duplexes',
                 'Block of Flats', 'Semi Detached Bungalow', 'Terraced Bungalow',
                 'Detached Bungalow']
unique_towns = ['Lekki', 'Ajah', 'Victoria Island (VI)', 'Ikeja', 'Magodo', 'Yaba',
               'Agege', 'Ikorodu', 'Isheri North', 'Isheri', 'Ikoyi', 'Ipaja',
               'Ibeju Lekki', 'Mushin', 'Ejigbo', 'Ojodu', 'Shomolu', 'Ogudu',
               'Isolo', 'Surulere', 'Alimosho', 'Ikotun', 'Maryland', 'Gbagada',
               'Idimu', 'Ifako-Ijaiye', 'Ojo', 'Kosofe', 'Ayobo', 'Ilupeju',
               'Ketu', 'Ojota', 'Oshodi', 'Amuwo Odofin', 'Agbara-Igbesa',
               'Ijaiye', 'Apapa', 'Lagos Island', 'Epe', 'Oke-Odo', 'Egbe',
               'Orile', 'Badagry', 'Ijesha']

# Create the Streamlit app
st.title("House Price Prediction")

# Create input fields for the features
bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, step=1)
toilets = st.number_input("Number of Toilets", min_value=1, step=1)
parking_space = st.number_input("Number of Parking Spaces", min_value=1, step=1)
title = st.selectbox("Title", unique_titles)
town = st.selectbox("Town", unique_towns)
state = st.text_input("State")

# Create a button to trigger the prediction
if st.button("Predict House Price"):
    # Create a new data frame with the input values
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'toilets': [toilets],
        'parking_space': [parking_space],
        'title': [title],
        'town': [town],
        'state': [state]
    })

    # Make the prediction
    predicted_price = model.predict(input_data)[0]

    # Display the predicted price
    st.write(f"The predicted house price is ₦{predicted_price:.2f}")
    