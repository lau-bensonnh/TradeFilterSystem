from io import StringIO
import pandas as pd
import psycopg2

# from src.DataSource.GetHistData = Get Daily Historical Data
from src.DataSource.GetHistData import initial_weekly_data
# from src.Calculation.ComputeMACD
from src.Calculation.ComputeMACD import compute_macd
from src.Calculation.ComputeMACD import check_macd

# from src.Calculation.STC
from src.Calculation.ComputeSTC import compute_stc
from src.Calculation.ComputeSTC import check_stc


ticker = "9988.hk"

# Grab Data
data = initial_weekly_data(ticker)
print(data)

# DATA CLEANSING
# Add ticker to the data, Rename DATE column, Remove Adj Close
data['Ticker'] = ticker
data = data.rename(columns={'Date': 'market_date'})
data = data.drop(columns=['Adj Close'])
print(data)
data['market_date'] = pd.to_datetime(data['market_date'])

# Calculate MACD
data = compute_macd(data, 12, 26, 9)
print(data)

# Check MACD Status
momentumCheck = check_macd(data)

# Calculate STC
data = compute_stc(data, 16, 8, 8)
print(data)

# Check STC Status
stcCheck = check_stc(data)
