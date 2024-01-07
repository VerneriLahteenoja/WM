import sqlite3
from sqlite3 import Error


class Operations():
    def __init__(self):
        database = "wm_db.db"
        
        try:
            self.connection = sqlite3.connect(database)
        except Error as e:
            print(str(e))
    
    def operation(self, statement):
        """insert to a table

        Args:
            statement (str): complete SQL Statement
        """

        try:
            cur = self.connection.cursor()
            cur.execute(statement)
            self.connection.commit()
        except Error as e:
            print(str(e))
        finally:
            print(cur.lastrowid)

    
if __name__=="__main__":
    Operations().operation("INSERT INTO profile(name) VALUES('tester');")
