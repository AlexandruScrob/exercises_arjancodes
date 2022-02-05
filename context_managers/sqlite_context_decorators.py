import logging
import sqlite3
from contextlib import contextmanager

from constants import DB_PATH


@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)

    try:
        cursor = connection.cursor()
        yield cursor
    finally:
        logging.info("Closing connection")
        connection.commit()
        connection.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name=DB_PATH) as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
