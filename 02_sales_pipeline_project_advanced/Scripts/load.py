import pandas as pd
from sqlalchemy  import create_engine

DataBase_URL = 'postgresql://postgres:[YOUR-PASSWORD]@db.psdthsthwvdoozwupijy.supabase.co:5432/postgres'

table_name = 'final_data'

def load_data(df_final):
    engine = create_engine(DataBase_URL)
    df_final.to_sql(
        name = table_name,
        con=engine,
        if_exists= "append",
        index=False
    )
    print('Data Loaded Sucessfully.')




