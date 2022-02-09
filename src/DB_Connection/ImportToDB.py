from io import StringIO
import pandas as pd


def exportdf(df, ticker):
    df.to_csv("$HOME/" + ticker + ".csv", index=False, header=True)
    return
