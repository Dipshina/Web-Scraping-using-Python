## Importing 'BeautifulSoup' class from 'bs4' library
## Importing 'requests' module for making http request

from bs4 import BeautifulSoup
import requests


## Sends HTTP GET request to the specified URL
## Store the response from the server in 'page' variable

page = requests.get(url)


## Navigate and extract information from the HTML structure of the page

soup = BeautifulSoup(page.text, 'html')


## Import the 'pandas' library and assigns it the alias 'pd'

import pandas as pd


## Pandas function used to create a new DataFrame

df = pd.DataFrame(columns = table_data_titles)


## Exports the DataFrame df to a CSV (Comma-Separated Values) file named 'gdp.csv'

df.to_csv('gdp.csv', index = False)


## Import the 'sqlite3' module in Python

import sqlite3


## Creates a connection to an SQLite database file named 'nepalgdp.db'

conn = sqlite3.connect('nepalgdp.db')


## 'cur' object represents the cursor that allows you to interact with the database

cur = conn.cursor()


##  DataFrame is converted into a record (a tuple) in the structured array

data_to_be_inserted = df.to_records(index = False)


## SELECT query on the 'nepalgdp' table and retrieve all rows from that table

cur.execute("Select * from nepalgdp").fetchall()




