from io import StringIO
import pandas as pd


def exportdf(df, ticker):
    homePath = "/Users/benson/"
    df.to_csv(homePath + ticker + ".csv", index=False, header=True)
    return
