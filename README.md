## Code Description:


### Imports 'BeautifulSoup' class from 'bs4' library
### Imports 'requests' module for making http request

```python
from bs4 import BeautifulSoup
import requests
```

### Sends HTTP GET request to the specified URL
### Stores the response from the server in 'page' variable

```python
page = requests.get(url)
```

### Navigates and extracts information from the HTML structure of the page

```python
soup = BeautifulSoup(page.text, 'html')
```

### Imports the 'pandas' library and assigns it the alias 'pd'

```python
import pandas as pd
```

### Pandas function used to create a new DataFrame

```python
df = pd.DataFrame(columns = table_data_titles)
```

### Exports the DataFrame df to a CSV (Comma-Separated Values) file named 'gdp.csv'

```python
df.to_csv('gdp.csv', index = False)
```

### Imports the 'sqlite3' module in Python

```python
import sqlite3
```

### Creates a connection to an SQLite database file named 'nepalgdp.db'

```python
conn = sqlite3.connect('nepalgdp.db')
```

### 'cur' object represents the cursor that allows you to interact with the database

```python
cur = conn.cursor()
```

###  DataFrame is converted into a record (a tuple) in the structured array

```python
data_to_be_inserted = df.to_records(index = False)
```

### SELECT query on the 'nepalgdp' table and retrieve all rows from that table

```python
cur.execute("Select * from nepalgdp").fetchall()
```



