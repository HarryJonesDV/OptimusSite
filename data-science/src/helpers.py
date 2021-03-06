"""Helper function to normalise and denormalise."""
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import src.topicmodel as tm


def encoders(raw_data):
    # Encoding the labels
    le_txt = preprocessing.LabelEncoder()

    # Normalising inputs and outputs
    in_scaler = MinMaxScaler(feature_range=(0, 1))
    out_scaler = MinMaxScaler(feature_range=(0, 1))

    return in_scaler, out_scaler, le_txt


def preprocess_training(raw_data, le_txt, in_scaler, out_scaler):
    # Separate inputs from outputs in training dataset
    #raw_data['text'] = le_txt.fit_transform(raw_data['text'])
    
    text_topics = tm.topic_matcher(raw_data['text'])
    raw_data['t0'] = text_topics['t0']
    raw_data['t1'] = text_topics['t1']
    raw_data['t2'] = text_topics['t2']
    raw_data['t3'] = text_topics['t3']
    raw_data['t4'] = text_topics['t4']

    inputs = raw_data.drop(['ctd'], axis=1).values
    outputs = raw_data[['ctd']].values

    # Scale both the training inputs and outputs
    in_scaled = in_scaler.fit_transform(inputs)
    out_scaled = out_scaler.fit_transform(outputs)

    return in_scaled, out_scaled


def preprocess_predict(raw_data, le_txt, in_scaler):
    # Separate inputs from outputs in training dataset
    #raw_data['text'] = le_txt.fit_transform(raw_data['text'])

    text_topics = tm.topic_matcher(raw_data['text'])
    raw_data['t0'] = text_topics['t0']
    raw_data['t1'] = text_topics['t1']
    raw_data['t2'] = text_topics['t2']
    raw_data['t3'] = text_topics['t3']
    raw_data['t4'] = text_topics['t4']

    inputs = raw_data.values

    # Scale both the training inputs and outputs
    in_scaled = in_scaler.fit_transform(inputs)

    return in_scaled


def training_test(in_scaled, out_scaled, out_scaler, size):
    in_training, in_test, out_training, out_test = train_test_split(
        in_scaled, out_scaled, test_size=size)
    return in_training, in_test, out_training, out_test
