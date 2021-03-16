from googlesearch import search
import pandas as pd

selected_league='premier league'
selected_year='2020'
query= selected_league + ' reference ' + selected_year

print(query)
for j in search(query, tld="com", num=1, stop=1, pause =2):
    url = j
html = pd.read_html(url, header =0)
df= html[0]
raw=df.drop(['Attendance','Last 5', 'Goalkeeper', 'Notes','GD','xGA','xGD'], axis = 1)
raw=-raw.rename(columns={'Squad':'Teams','Rk':'Pos'})
#raw = df.drop(df[df.Age == 'Age'].index) 
#raw = raw.fillna(0)
#playerstats = raw.drop(['Rk'], axis=1)
print(raw)

    