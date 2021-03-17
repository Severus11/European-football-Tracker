import streamlit as st
import numpy as np 
import pandas as pd 
import base64
from googlesearch import search
import matplotlib.pyplot as plt 

st.title('Premier League Tracker')

st.markdown('''This app performs simple webscraping of Premier League teams data!

* **Data source:** [fbref.com](https://fbref.com/en/comps/9/Premier-League-Stats).''')

st.sidebar.header('User input features')

list_league = ['Premier League', 'Bundesliga', 'La Liga','Ligue 1', 'Serie A']
selected_league = st.sidebar.selectbox('Select league', ('Premier League', 'Bundesliga', 'La Liga','Ligue 1', 'Serie A'))
selected_year = st.sidebar.selectbox('Choose Season', list(reversed(range(1950, 2020 ))))

@st.cache
def load_data(league, year):
    global url
    query= league + 'reference' + str(year) 
    for j in search(query, tld="com", num=1, stop=1, pause =1):
        url = j   
    #url = load_query(query)
    html = pd.read_html(url, header =0)
    df= html[0]
    raw=df[['Rk','Squad','MP','W', 'D','L','GF','GA','Pts','xG','Top Team Scorer']]
    rankings_table=raw.rename(columns={'Squad':'Teams','Rk':'Pos'})
    return rankings_table

league_rankings= load_data(selected_league,selected_year)
print(league_rankings)

teams = sorted(league_rankings.Teams.unique())
selected_team = st.sidebar.multiselect('Teams', teams, teams)

df_selected_team = league_rankings[(league_rankings.Teams.isin(selected_team))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="standings.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)