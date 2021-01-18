from io import StringIO
import pandas as pd
import psycopg2

# from src.DataSource.GetHistData import update_daily_data
from src.DataSource.GetHistData import initial_daily_data

ticker = "9988.hk"
data = initial_daily_data(ticker)
print(data)

data['Ticker'] = ticker
data = data.rename(columns={'Date': 'market_date'})
data = data.drop(columns=['Adj Close'])
print(data)
data['market_date'] = pd.to_datetime(data['market_date'])
datatypes = data.dtypes
print(datatypes)
buf = StringIO()
data.to_csv(buf, header=False, index=False)
buf.seek(0)
print(buf)

conn = psycopg2.connect("host=localhost dbname=tfs_dev user=tfs_dev password=ehYY76wd")
cur = conn.cursor()
cur.copy_from(buf, 'hist_data', columns=('market_date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker'), sep=',')
cur.execute('commit')
