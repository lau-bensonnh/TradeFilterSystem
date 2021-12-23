# Reference
# https://stackoverflow.com/questions/48023982/pandas-finding-local-max-and-min
# https://medium.datadriveninvestor.com/how-to-algorithmically-detect-technical-chart-patterns-155ca13b7b26

import pandas as pd
from scipy.signal import argrelextrema
import numpy as np

def holyGrail(df,n):

    # find local peak
    df['Local Low'] = df.iloc[argrelextrema(df.Low.values, np.less_equal,order=n)[0]]['Low']
    df['Local High'] = df.iloc[argrelextrema(df.High.values, np.greater_equal,order=n)[0]]['High']

    return df