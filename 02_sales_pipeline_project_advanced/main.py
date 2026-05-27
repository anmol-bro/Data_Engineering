from Scripts.extract import extract_api_data, extract_csv_data
from Scripts.transform import transform_data
from Scripts.load import load_data

def run_pipeline():
    df_a = extract_api_data()
    df_c = extract_csv_data('data/sales_data.csv')
    df_transformed = transform_data(df_c,df_a)
    load_data(df_transformed)

if __name__ == "__main__":
    run_pipeline()
