import streamlit as st
from operator import mod
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Model Interactions", 
    page_icon="🌈", 
    layout="wide",
    initial_sidebar_state="expanded"
)
# from lesson 10.02
# function to load models
@st.cache
def load_model_a():
  with open('../models/a_model_xgb.pkl', 'rb') as f:
    a_model = pickle.load(f)
  return a_model

def load_model_h():
  with open('../models/h_model_xgb.pkl', 'rb') as f:
    h_model = pickle.load(f)
  return h_model

# assign models to value
a_model = load_model_a()
h_model = load_model_h()

st.title('Predict a Trackpoint\'s Heart Rate')

st.subheader('Input required fields below to make a heart rate predictions!')

pred_df = pd.read_csv('../data/ah_pred_df.csv')
temperature = st.text_area('Enter the temperature (Kelvins) here.')
