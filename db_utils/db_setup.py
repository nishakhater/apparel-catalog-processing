# ONLY RUN THIS FILE IF YOU ARE SETTING UP THE PROJECT FOR THE FIRST TIME

from contextlib import closing
from sqlite3 import Connection
from subcategories_dao import add_category
from constants import ALL_DRESSES, ALL_BAGS, ALL_HOME, ALL_JEWELRY, ALL_PANTS, ALL_PERFUMES, ALL_SHOES, ALL_TOPS

def build_categories(conn: Connection):
    for dress in ALL_DRESSES:
        add_category(conn, dress, "Dresses")
    for bag in ALL_BAGS:
        add_category(conn, bag, "Bags")
    for home in ALL_HOME:
        add_category(conn, home, "Home Decor")
    for jewelry in ALL_JEWELRY:
        add_category(conn, jewelry, "Jewelry")
    for pants in ALL_PANTS:
        add_category(conn, pants, "Pants")
    for perfumes in ALL_PERFUMES:
        add_category(conn, perfumes, "Perfumes")
    for shoes in ALL_SHOES:
        add_category(conn, shoes, "Shoes")
    for top in ALL_TOPS:
        add_category(conn, top, "Tops")


def build_tables(conn: Connection):
    sql = """
    CREATE TABLE IF NOT EXISTS subcategories (
	subcategory varchar(100),
	category varchar(100))
    """
    with closing(conn.cursor()) as cur:
        cur.execute(sql)


def main():
    build_tables()
    build_categories()

main()