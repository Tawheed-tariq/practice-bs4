import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)

soup = BeautifulSoup(r.text , 'html.parser')

#get table which contains data
table = soup.find("table", class_ = 'ih-td-tab auction-tbl')

#get table headers
title = table.find_all('th')

header = []
for i in title:
    name = i.text
    header.append(name)


#creating a data frame
df = pd.DataFrame(columns=header)
# print(df)

# get table rows
rows = table.find_all('tr')

# getting table rows except table heading , hence we collect data from 1st tr
for i in rows[1:]: 
    first_td = i.find_all('td')[0].find('div', class_ = 'ih-pt-ic').text.strip()
    #we were getting '\n\n\n' in the team names, so here we are getting the team names 
    # and using strip() method , we are removing all the white spaces

    data = i.find_all('td')[1:] # here we dont want the data of team name because we already got that
    row = [tr.text for tr in data]
    row.insert(0, first_td) # insert team name at first
    l = len(df)
    df.loc[l] = row
# convert the data frame into csv
# df.to_csv('Ipl-data.csv')
