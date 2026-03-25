import sqlite3

def load_data(df , db_name = 'sales.db'):
    conn = sqlite3.connect(db_name)
    df.to_sql('sales',conn, if_exists="replace", index=False)
    conn.close()