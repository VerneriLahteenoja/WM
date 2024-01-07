# CREATE DATABASE
import sqlite3
from sqlite3 import Error


def create_database(db_file: str):
    """create a database

    Args:
        db_file (str): <name of the database to create>
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


if __name__=="__main__":
    create_database("wm_db.db")