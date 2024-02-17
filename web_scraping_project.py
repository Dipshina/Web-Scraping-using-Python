# -*- coding: utf-8 -*-
"""Web Scraping Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X-qwWS5rYD5qQCFu9S4xTYhircIKVixT
"""

from bs4 import BeautifulSoup
import requests

# Assigning url string
url = "https://www.worldometers.info/gdp/nepal-gdp/"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

table = soup.find_all('table')

soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')

data_titles = soup.find_all('th')

data_titles

table_data_titles = [title.text for title in data_titles]

table_data_titles

import pandas as pd

df = pd.DataFrame(columns = table_data_titles)

column_data = soup.find_all('tr')

for row in column_data[3:]:
  row_data = row.find_all('td')
  table_row_data = [data.text for data in row_data]

  length = len(df)
  df.loc[length] = table_row_data

df

"""# Scraping into csv file"""

df.to_csv('gdp.csv', index = False)

"""# Scraping into Database"""

import sqlite3

conn = sqlite3.connect('nepalgdp.db')

cur = conn.cursor()

data_to_be_inserted = df.to_records(index = False)

query = """
CREATE TABLE nepalgdp (
    Year INTEGER,
    GDP_Nominal_Current_USD INTEGER,
    GDP_Real_Inflation_adj INTEGER,
    GDP_change DECIMAL(4,2),
    GDP_per_capita INTEGER,
    Pop_change DECIMAL(4,2),
    Population INTEGER
);
"""

query = """
INSERT INTO nepalgdp (Year, GDP_Nominal_Current_USD, GDP_Real_Inflation_adj, GDP_change, GDP_per_capita, Pop_change, Population)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

try:
    for row_data in data_to_be_inserted:
        cur.execute(query, row_data)
    conn.commit()
except Exception as e:
    print(e)

cur.execute("Select * from nepalgdp").fetchall()
