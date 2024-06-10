import streamlit as st
import pickle
import pandas as pd

from data_preprocessor import preprocess_data

# Load the saved model
with open('lr_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

with open('gb_model.pkl', 'rb') as f:
    gb_model = pickle.load(f)

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
st.title("Lagos House Price Prediction")

sys = st.radio("Select Model", ('Linear Regression', 'Gradient Boosting'))

# Create input fields for the features
bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, step=1)
toilets = st.number_input("Number of Toilets", min_value=1, step=1)
parking_space = st.number_input("Number of Parking Spaces", min_value=1, step=1)
title = st.selectbox("Type", unique_titles)
town = st.selectbox("Town", unique_towns)

# Create a button to trigger the prediction
if st.button("Predict House Price"):
    # Create a new data frame with the input values
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'toilets': [toilets],
        'parking_space': [parking_space],
        'title': [unique_titles.index(title)],
        'town': [unique_towns.index(town)]
    })
    # X_data = preprocess_data(input_data)

    # Make the prediction
    # predicted_price = lr_model.predict(input_data)[0]

    # # Display the predicted price
    # st.write(f"The predicted house price is ₦{predicted_price:.2f}")

    if sys == 'Linear Regression':
        try:
            # with st.spinner('Crunching the numbers...'):
            #     top_recommendations = content_model(movie_list=fav_movies,
            #                                         top_n=13)

            
            # Make the prediction
            predicted_price = lr_model.predict(input_data)[0]
            predicted_price = round(predicted_price)
            predicted_price = "{:,}".format(predicted_price)
            st.write(f"### The predicted house price is ₦{predicted_price}")
            
        except:
            st.error("Oops! Looks like this algorithm does't work.\
                        We'll need to fix it!")


    if sys == 'Gradient Boosting':
        try:
            predicted_price = gb_model.predict(input_data)[0]
            predicted_price = round(predicted_price)
            predicted_price = "{:,}".format(predicted_price)
            st.write(f"### The predicted house price is ₦ {predicted_price}")

        except:
            st.error("Oops! Looks like this algorithm does't work.\
                        We'll need to fix it!")


    