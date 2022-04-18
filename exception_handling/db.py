import sqlite3


# TODO using context manager with sqlite
class SQLite:
    def __init__(self, file="application.db"):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


class NotFoundError(Exception):
    pass


class NotAuthorizedError(Exception):
    pass


def blog_lst_to_json(item):
    return {
        "id": item[0],
        "published": item[1],
        "title": item[2],
        "content": item[3],
        "public": bool(item[4]),
    }


def fetch_blogs():
    try:
        with SQLite("application.db") as cur:
            # execute the query
            cur.execute("SELECT * FROM blogs where public=1")

            # fetch the data and turn into a dict
            result = list(map(blog_lst_to_json, cur.fetchall()))

            return result

    except sqlite3.OperationalError as ex:
        print(ex)
        return []


def fetch_blog(_id: str):
    try:
        # connect to the database
        con = sqlite3.connect("application.db")
        cur = con.cursor()

        # execute the query and fetch the data
        cur.execute(f"SELECT * FROM blogs where id=?", [_id])
        result = cur.fetchone()

        if result is None:
            raise NotFoundError(f"Unable to find blog with id {_id}.")

        data = blog_lst_to_json(result)

        if not data["public"]:
            raise NotAuthorizedError(
                f"You're not allowed to " f"access blog with id {_id}."
            )

        return data

    except sqlite3.OperationalError as ex:
        print(ex)
        raise NotFoundError(f"Unable to find blog with id {_id}.")

    finally:
        # close the db
        con.close()
