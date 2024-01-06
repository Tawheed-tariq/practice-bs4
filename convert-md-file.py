import pandas as pd
import requests
from bs4 import BeautifulSoup
header = []
url = "https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

table = soup.find('table', class_ = 'ws-table-all notranslate')
title = table.find_all('th')
rows = table.find_all('tr')
for i in title:
    header.append(i.text)

df = pd.DataFrame(columns=header)  

for i in rows[1:]:
    property = i.find_all('td')[0].text
    desc = i.find_all('td')[1].text.split('\n') 
    description = (" ".join(desc)) 
    row = [property, description]
    l = len(df)
    df.loc[l] =  row
df.to_markdown('dataframe.md')