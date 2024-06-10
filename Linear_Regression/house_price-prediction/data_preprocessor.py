import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_data(df):
    """
    Preprocess the input DataFrame by encoding categorical features and rescaling the X feature.
    
    Args:
        df (pandas.DataFrame): The input DataFrame.
        
    Returns:
        X (numpy.ndarray): The preprocessed X feature.
    """
    # Encode categorical features
    label_encoder = LabelEncoder()
    df['title'] = label_encoder.fit_transform(df['title'])
    df['town'] = label_encoder.fit_transform(df['town'])
    
    # Rescale the X feature
    scaler = MinMaxScaler()
    X = scaler.fit_transform(df)
    
    
    return X
