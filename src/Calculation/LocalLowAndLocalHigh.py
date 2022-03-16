# Reference
# https://stackoverflow.com/questions/48023982/pandas-finding-local-max-and-min
# https://medium.datadriveninvestor.com/how-to-algorithmically-detect-technical-chart-patterns-155ca13b7b26

import pandas as pd
from scipy.signal import argrelextrema
import numpy as np


def holyGrail(df, n):
    # find local peak for n bars in before and after
    df['Local Low'] = df.iloc[argrelextrema(df.Low.values, np.less_equal, order=n)[0]]['Low']
    df['Local High'] = df.iloc[argrelextrema(df.High.values, np.greater_equal, order=n)[0]]['High']

    rowcount= len(df.index)
    print(rowcount)

    # n bars after local high, no need local low
    for x in range(rowcount-200, rowcount):
        trend_high = True
        trend_low = True
        if not pd.isna(df['Local Low'].iloc[x - n]):
            for y in range(x - n, x):
                if not pd.isna(df['Local High'].iloc[y]):
                    trend_low = False
            if trend_low:
                # df['Local Low'].iloc[x] = df['Low'].iloc[x]
                df.loc[x, 'Local Low'] = 'Low'

        if not pd.isna(df['Local High'].iloc[x-n]):
            for y in range(x - n, x):
                if not pd.isna(df['Local Low'].iloc[y]):
                    trend_high = False
            if trend_high:
                # df['Local High'].iloc[x] = df['High'].iloc[x]
                df.loc[x, 'Local High'] = 'High'

    return df
