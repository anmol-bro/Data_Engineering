import pandas as pd


def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df['total_sales'] = df['price'] * df['quantity']
    df['date'] = pd.to_datetime(df['date'],errors="coerce")
    return df

