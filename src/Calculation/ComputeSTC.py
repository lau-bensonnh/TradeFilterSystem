import pandas as pd


def compute_stc(df, period, n_d, n_smooth):
    df['14-high'] = df['High'].rolling(period).max()
    df['14-low'] = df['Low'].rolling(period).min()
    df['Fast%K'] = (df['Close'] - df['14-low']) * 100 / (df['14-high'] - df['14-low'])
    df['Slow%K'] = df['Fast%K'].rolling(n_d).mean()
    df['Slow%D'] = df['Fast%K'].rolling(n_smooth).mean()
    return df
