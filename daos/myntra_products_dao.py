from contextlib import closing
from sqlite3 import Connection
import pandas as pd


def add_products(conn: Connection, df: pd.DataFrame) -> None:
    df = df.rename(columns={
        'ProductName': 'name', 
        'ProductID': 'product_id',
        'ProductBrand': 'brand',
        'Gender': 'gender',
        'Price (INR)': 'price',
        'Description': 'description',
        'PrimaryColor': 'primary_color',
        'Category': 'category'
        })
    df.to_sql('myntra_products', con=conn, if_exists='append', index=False)