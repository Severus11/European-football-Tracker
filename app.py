import streamlit as st
import numpy as np 
import pandas as pd 
import base64
import googlesearch
import matplotlib.pyplot as plt 

st.title('Premier League Tracker')

st.markdown('''This app performs simple webscraping of Premier League teams data!
* 
* **Data source:** [fbref.com](https://fbref.com/en/comps/9/Premier-League-Stats).''')

st.sidebar.header('User input features')

list_league = ['Premier League', 'Bundesliga', 'La Liga','Ligue 1', 'Serie A']
selected-league = st.sidebar.selectbox('Select league', list_league,list_league )
selected-year = st.sidebar.selectbox('Choose Season', list(reversed(range(1950, 2020))))

@st.cache
def load_data(year):
    query= selected-league + 'reference' + selected-year
    