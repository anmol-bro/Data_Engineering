import pandas as pd 
import requests

def extract_csv_data(path):
    try:
        df_csv = pd.read_csv(path)
        print(f"[info] Loaded CSV: {len(df_csv)} rows")
        return df_csv
    except FileNotFoundError:
        print(f'[error] File not Found: {path}')
        return pd.DataFrame()
    
def extract_api_data():
    try:
        products = requests.get("https://kolzsticks.github.io/Free-Ecommerce-Products-Api/main/products.json").json()
        return products
    except  requests.exceptions.RequestException as e:
        print(f"[error] API request Failed, {e}")
        return pd.DataFrame()

