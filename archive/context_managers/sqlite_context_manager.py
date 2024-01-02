import logging
import sqlite3

from constants import DB_PATH


class SQLite:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)

    def __enter__(self):
        logging.info("Calling __enter__")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with SQLite(file_name=DB_PATH) as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
