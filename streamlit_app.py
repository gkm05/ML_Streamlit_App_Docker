import streamlit as st
import pandas as pd
import numpy as np
import pickle

#st.title('Hello, Streamlit!')
#st.write('This is a test to see if the app is running.')

# Load your trained model
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title('Iris Flower Classification using Pre-Trained Model')

# Sidebar for user input
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input
st.subheader('User Input Parameters')
st.write(input_df)

# Predict
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Output
st.subheader('Prediction')
#iris_target = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
st.write(prediction[0])

st.subheader('Prediction Probability')
st.write(prediction_proba)
