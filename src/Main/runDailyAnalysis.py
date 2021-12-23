from io import StringIO
import pandas as pd
import psycopg2

# from src.DataSource.GetHistData = Get Daily Historical Data
from src.DataSource.GetHistData import initial_daily_data
# from src.Calculation.ComputeMACD
from src.Calculation.ComputeMACD import computeMACD
# from src.Calculation.STC
from src.Calculation.ComputeSTC import compute_stc


ticker = "9988.hk"
data = initial_daily_data(ticker)
print(data)

# DATA CLEANSING
# Add ticker to the data, Rename DATE column, Remove Adj Close
data['Ticker'] = ticker
data = data.rename(columns={'Date': 'market_date'})
data = data.drop(columns=['Adj Close'])
print(data)
data['market_date'] = pd.to_datetime(data['market_date'])

# Calculate MACD
data = computeMACD(data, 12, 26, 9)
print(data)

# Calculate STC
data = compute_stc(data, 16, 8, 8)
print(data)





