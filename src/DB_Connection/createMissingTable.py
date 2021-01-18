import psycopg2


conn = psycopg2.connect("host=localhost dbname=tfs_dev user=tfs_dev password=ehYY76wd")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS ticker(
    id SERIAL PRIMARY KEY,
    ticker text UNIQUE NOT NULL,
    category text,
    exchange text,
    country text
)
""")
cur.execute('commit')
cur.execute("""
    CREATE TABLE IF NOT EXISTS hist_data(
    id SERIAL PRIMARY KEY,
    Ticker text NOT NULL,
    Market_Date date NOT NULL,
    Open float NOT NULL,
    High float NOT NULL,
    Low float NOT NULL,
    Close float NOT NULL,
    Volume float,
    MACD float,
    MACD_Ref float,
    MACD_Histo float,
    STC float,
    STC_Ref float
)
""")
cur.execute('commit')
