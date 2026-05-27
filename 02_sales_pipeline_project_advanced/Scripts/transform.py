import pandas as pd


def transform_data(df_csv, df_apin):
    df_api = pd.json_normalize(df_apin)                    #flattening the json
    df_api = pd.DataFrame(df_api)
    df_csv['id'] = df_csv['id'].astype(str)
    df_api['id'] = df_api['id'].astype(str)
    df_api = df_api.rename(columns={                      #renaming column names in a better way after flattening
        'rating.stars' : 'rating_stars',
        'rating.count' : 'rating_count'
    })
    df_api["keywords"] = df_api["keywords"].apply(lambda x : "|".join(x))
    df_merged = pd.merge(df_api , df_csv , on='id', how='left')
    df_merged["price"] = df_merged["priceCents"]/100
    df_merged["discounted_price"] = df_merged["price"] - ((df_merged["price"] * df_merged["discount_percent"])/100)
    df_merged["stock_status"] = 'NA'#df_merged.apply(lambda x : "In Stock" if df_merged['stock']>50 else ("Low Stock" if df_merged['stock']<50 else "Out of Stock" ))
    df_merged["inventory_value"] = df_merged['stock_quantity'] * df_merged["discounted_price"]
    df_merged["popularity_score"] = df_merged['rating_stars'] * df_merged['rating_count']
    df_merged = df_merged[df_merged["is_active"]==True]

    df_final = df_merged[['id',
                           'name', 
                           'category',
                            'subCategory',
                            'price', 
                            'discounted_price',
                            'stock_quantity',
                            'stock_status',
                            'warehouse_location', 
                            'supplier_name',
                            'rating_stars', 
                            'rating_count',
                            'popularity_score',
                            'inventory_value']]
    return df_final




    