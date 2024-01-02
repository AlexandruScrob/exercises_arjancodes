import logging
import sqlite3

from constants import DB_PATH


def main():
    logging.basicConfig(level=logging.INFO)
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())
    finally:
        logging.info("Closing connection")
        connection.close()


if __name__ == "__main__":
    main()
