# Lagos House Price Prediction App

This Streamlit web application predicts house prices in Lagos based on input features such as the number of bedrooms, bathrooms, toilets, parking spaces, type of property, and location.

## Models Available
You can select between two models for prediction:
- **Linear Regression**
- **Gradient Boosting**

## Input Features
- **Number of Bedrooms**
- **Number of Bathrooms**
- **Number of Toilets**
- **Number of Parking Spaces**
- **Type of Property**
- **Location (Town)**

### Type of Properties
- Detached Duplex
- Semi Detached Duplex
- Terraced Duplexes
- Block of Flats
- Semi Detached Bungalow
- Terraced Bungalow
- Detached Bungalow

### Locations (Towns)
- Lekki
- Ajah
- Victoria Island (VI)
- Ikeja
- Magodo
- Yaba
- and many more

## Instructions
1. Fill in the input fields.
2. Select the model you want to use.
3. Click the "Predict House Price" button to see the prediction.

## Repository Contents
- **Data Preprocessing**: `data_preprocessor.py` script for encoding categorical features and rescaling data.
- **Models Directory**: Contains trained models for prediction.
  - `gb_model.pkl`: Gradient Boosting model.
  - `lr_model.pkl`: Linear Regression model.
- **Jupyter Notebook**: `house_price.ipynb` for data analysis and model development.
- **Dataset**: `price_data.csv` containing property details and prices.
- **Streamlit App**: `price_prediction.py` for interactive house price predictions.

## Usage
1. **Data Preprocessing**:
   - Use `data_preprocessor.py` to preprocess your data before training the models.
2. **Models**:
   - Trained models are saved in the `models` directory. Load them for predictions.
3. **Jupyter Notebook**:
   - Explore `house_price.ipynb` for detailed analysis and insights.
4. **Dataset**:
   - The `price_data.csv` file contains the dataset used for training.
5. **Streamlit App**:
   - Run `price_prediction.py` to launch the interactive house price prediction app.

## Note
Please make sure you have the necessary data files and models in their respective directories before running the app.

---

*Feel free to contribute, report issues, or suggest improvements for the House Price Prediction App in Lagos!*
