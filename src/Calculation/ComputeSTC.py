import pandas as pd
import numpy as np

def compute_stc(df, period, n_d, n_smooth):
    df['14-high'] = df['High'].rolling(period).max()
    df['14-low'] = df['Low'].rolling(period).min()
    df['Fast%K'] = (df['Close'] - df['14-low']) * 100 / (df['14-high'] - df['14-low'])
    df['Slow%K'] = df['Fast%K'].rolling(n_d).mean()
    df['Slow%D'] = df['Slow%K'].rolling(n_smooth).mean()
    df['Slow%KGradient'] = np.gradient(df['Slow%K'].rolling(center=False, window=3).mean)
    return df

def check_stc(df):
    if df['Slow%K', -1] > df['Slow%K', -2]:
        stc_status = 'Upward'
    else:
        stc_status = 'downward'
    if (df['Slow%KGradient', -2] > 0 > df['Slow%KGradient', -1]) or (
            df['Slow%KGradient', -2] < 0 < df['Slow%KGradient', -1]):
        stc_status = stc_status + ' just turned'

    return stc_status
