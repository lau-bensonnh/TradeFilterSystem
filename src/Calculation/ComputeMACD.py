import pandas as pd


def compute_macd(df, n_fast, n_slow, n_smooth):
    data = df['Close']

    fast_ema = data.ewm(span=n_fast, min_periods=n_slow).mean()
    slow_ema = data.ewm(span=n_slow, min_periods=n_slow).mean()
    macd = pd.Series(fast_ema - slow_ema, name='macd')
    macd_sig = pd.Series(macd.ewm(span=n_smooth, min_periods=n_smooth).mean(), name='macd_sig')
    macd_hist = pd.Series(macd - macd_sig, name='macd_hist')
    df = df.join(macd)
    df = df.join(macd_sig)
    df = df.join(macd_hist)

    return df


def check_macd(df):

    if df['macd'].iloc[-1] < 0:
        macd_status = 'Downtrend'
        if df['macd'].iloc[-2] < df['macd'].iloc[-1]:
            macd_status = macd_status + ' Momentum reducing'
            if abs((df['macd'].iloc[-1] - df['macd'].iloc[-2]) / df['macd'].iloc[-2]) < 0.05:
                macd_status = macd_status + ' & Flattening'
            if df['macd_hist'].iloc[-2] < df['macd_hist'].iloc[-1]:
                macd_status = macd_status + ' with deceleration'
            else:
                macd_status = macd_status + ' with acceleration'
        else:
            macd_status = macd_status + ' Momentum Increasing'
            if abs((df['macd'].iloc[-1] - df['macd'].iloc[-2]) / df['macd'].iloc[-2]) < 0.05:
                macd_status = macd_status + ' & Flattening'
            if df['macd_hist'].iloc[-2] < df['macd_hist'].iloc[-1]:
                macd_status = macd_status + ' with deceleration'
            else:
                macd_status = macd_status + ' with acceleration'
    else:
        macd_status = 'Uptrend'
        if df['macd'].iloc[-2] > df['macd'].iloc[-1]:
            macd_status = macd_status + ' Momentum Reducing'
            if abs((df['macd'].iloc[-2] - df['macd'].iloc[-1]) / df['macd'].iloc[-2]) < 0.05:
                macd_status = macd_status + ' & Flattening'
            if df['macd_hist'].iloc[-2] > df['macd_hist'].iloc[-1]:
                macd_status = macd_status + ' with deceleration'
            else:
                macd_status = macd_status + ' with acceleration'
        else:
            macd_status = macd_status + ' Momentum increasing'
            if abs((df['macd'].iloc[-2] - df['macd'].iloc[-1]) / df['macd'].iloc[-2]) < 0.05:
                macd_status = macd_status + ' & Flattening'
            if df['macd_hist'].iloc[-2] > df['macd_hist'].iloc[-1]:
                macd_status = macd_status + ' with deceleration'
            else:
                macd_status = macd_status + ' with acceleration'

    return macd_status
