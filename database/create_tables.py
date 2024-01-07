# CREATE DATABASE TABLES
import sqlite3
from sqlite3 import Error


def create_connection(db_file: str):
    """create database connection

    Args:
        db_file (str): database file to connect to

    Returns:
        Object/None: database object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(str(e))
    return connection

def create_table(connection, create_table_sql: str):
    """create table

    Args:
        connection (Object): Connection object
        create_table_sql (str): CREATE TABLE statement
    """
    try:
        cur = connection.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(str(e))

def main(table_list: list):

    database = "wm_db.db"

    conn = create_connection(database)

    if conn is not None:
        for statement in table_list:
            create_table(conn, statement)
    else:
        print("No database connection")
    

if __name__=="__main__":
    # SQL TABLE CREATION STATEMENTS
    STATEMENTS = [
    """CREATE TABLE IF NOT EXISTS profile (
        id integer PRIMARY KEY,
        name text NOT NULL
    )""",
    """CREATE TABLE IF NOT EXISTS weight (
        weight_id integer PRIMARY KEY,
        weight real NOT NULL,
        weight_date text NOT NULL,
        profile_id integer NOT NULL,
        FOREIGN KEY (profile_id) REFERENCES profile (id)
    )"""
    ]
    
    main(STATEMENTS)