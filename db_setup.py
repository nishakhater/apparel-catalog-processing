# ONLY RUN THIS FILE IF YOU ARE SETTING UP THE PROJECT FOR THE FIRST TIME

from contextlib import closing
from sqlite3 import Connection
from daos import subcategories_dao
from constants.constants import ALL_DRESSES, ALL_BAGS, ALL_HOME, ALL_JEWELRY, ALL_PANTS, ALL_PERFUMES, ALL_SHOES, ALL_TOPS

def build_categories(conn: Connection):
    for dress in ALL_DRESSES:
        subcategories_dao.add_category(conn, dress, "Dresses")
    for bag in ALL_BAGS:
        subcategories_dao.add_category(conn, bag, "Bags")
    for home in ALL_HOME:
        subcategories_dao.add_category(conn, home, "Home Decor")
    for jewelry in ALL_JEWELRY:
        subcategories_dao.add_category(conn, jewelry, "Jewelry")
    for pants in ALL_PANTS:
        subcategories_dao.add_category(conn, pants, "Pants")
    for perfumes in ALL_PERFUMES:
        subcategories_dao.add_category(conn, perfumes, "Perfumes")
    for shoes in ALL_SHOES:
        subcategories_dao.add_category(conn, shoes, "Shoes")
    for top in ALL_TOPS:
        subcategories_dao.add_category(conn, top, "Tops")


def build_categories_table(conn: Connection):
    sql = """
    CREATE TABLE IF NOT EXISTS subcategories (
	subcategory varchar(100),
	category varchar(100))
    """
    with closing(conn.cursor()) as cur:
        cur.execute(sql)


def build_products_table(conn: Connection):
    sql = """
    CREATE TABLE IF NOT EXISTS myntra_products (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	product_id INTEGER,
    name TEXT,
    brand varchar(200),
    gender varchar(100),
    price INTEGER,
    description TEXT,
    primary_color varchar(100),
	category varchar(100)
    )
    """
    with closing(conn.cursor()) as cur:
        cur.execute(sql)


def setup(conn: Connection):
    build_categories_table(conn)
    build_products_table(conn)
    build_categories(conn)