from contextlib import closing
from sqlite3 import Connection


def add_category(conn: Connection, subcategory: str, category: str):
    sql = """
        INSERT INTO subcategories (
            subcategory,
            category
        ) values (
            :subcategory,
            :category
        )
        """
    params = {
        "subcategory": subcategory,
        "category": category,
    }
    with closing(conn.cursor()) as cur:
        cur.execute(sql, params)
        conn.commit()


def get_category_and_subcategory(conn: Connection, keyword: str):
    sql = """
        SELECT subcategory, category FROM subcategories
        WHERE TRIM(LOWER(:keyword)) LIKE TRIM(LOWER('%' || subcategory || '%'))
        LIMIT 1
        """
    params = {
        "keyword": keyword,
    }

    with closing(conn.cursor()) as cur:
        result = cur.execute(sql, params).fetchone()
        return dict(zip([c[0] for c in cur.description], result)) if result else {}