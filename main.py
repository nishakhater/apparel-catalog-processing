from sqlite3 import Connection, Error
import sqlite3
import pandas as pd
import numpy as np
import subcategories_dao


# Takes in a dataframe and returns the dataframe with categories attached
# to it
def categorize(conn: Connection, df: pd.DataFrame) -> pd.DataFrame:
    def categorize_helper(row):
        name = row['ProductName']
        categories = subcategories_dao.get_category_and_subcategory(conn, name)
        return categories.get('category')

    df["Category"] = np.nan
    df["Category"] = df.apply(lambda row: categorize_helper(row), axis=1)

        


# Removes the brand from the product title if it is present
def remove_brand_from_name(df: pd.DataFrame) -> pd.DataFrame:
    def remove_brand(row):
        brand = row['ProductBrand']
    df["ProductName"] = df.apply(lambda row: remove_brand(row), axis=1)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def main():
    conn = create_connection('products.db')
    df = pd.read_csv('myntra_products_catalog.csv')

    # add categories to the dataframe of products
    categorize(conn, df)
    

main()