import datetime
from yahoo_historical import Fetcher

def initial_daily_data(ticker: str):
    start_yy = 1900
    start_mm = 1
    start_dd = 1
    data = Fetcher(ticker, [start_yy, start_mm, start_dd], None, "1d")
    #print(data.get_historical())
    return data.get_historical()

def update_daily_data(ticker: str, last_import_date):
    start_yy = last_import_date.year
    start_mm = last_import_date.month
    start_dd = last_import_date.day
    data = Fetcher(ticker, [start_yy, start_mm, start_dd], None, "1d")
    # print(data.get_historical())
    return data.get_historical()


x = datetime.datetime(2020,1,1)
data1 = update_daily_data("AAPL",x)
print(data1)

data2 = initial_daily_data("9988.hk")
print(data2)
