#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:56:38 2022

@author: adrianamachado
"""

# streamlit run streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/sandbox/a_1728.csv')

total_km = round(df.iloc[-1]['total_dist_km'], 2)
total_time = round((df.iloc[-1]['total_time_s']/60), 2)

st.title('August 06, 2022')
st.subheader(f'Total distance: {total_km} km')
st.subheader(f'Total distance: {total_time} minutes')

st.header('Route Simple Plot')
st.map(data = df['latitude', 'longitude', 'heart_rate'], zoom = 11)

st.header('Dataframe (you can move my parts around)')
st.dataframe(df)