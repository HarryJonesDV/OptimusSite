import pandas as pd 
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 

def encoders(raw_data):
    # Encoding the labels
    le_txt = preprocessing.LabelEnconder()

    # Normalising inputs and outputs
    in_scaler = MinMaxScaler(feature_range=(0,1))
    out_scaler = MinMaxScaler(feature_range=(0,1))

    return in_scaler, out_scaler, le_txt

def preprocess_training(raw_data, le_txt, in_scaler, out_scaler):
    # Separate inputs from outputs in training dataset
    raw_data['text'] = le_txt.fit_transform(raw_data['text'])
    
    inputs = raw_data.drop(['ctd'], axis=1).values
    outputs = raw_data[['ctd']].values

    # Scale both the training inputs and outputs
    in_scaled = in_scaler.fit_transform(inputs)
    out_scaled = out_scaler.fit_transform(outputs)

    return in_scaled, out_scaled

def preprocess_training(raw_data, le_txt, in_scaler, out_scaler):
    # Separate inputs from outputs in training dataset
    raw_data['text'] = le_txt.fit_transform(raw_data['text'])
    
    inputs = raw_data.drop(['ctd'], axis=1).values
    outputs = raw_data[['ctd']].values

    # Scale both the training inputs and outputs
    in_scaled = in_scaler.fit_transform(inputs)
    out_scaled = out_scaler.fit_transform(outputs)

    return in_scaled, out_scaled

def training_test(in_scaled, out_scaled, out_scaler, size):

    in_training, in_test, out_training, out_test = train_test_split(in_scaled, out_scaled, test_size = size)
    return in_training, in_test, out_training, out_test