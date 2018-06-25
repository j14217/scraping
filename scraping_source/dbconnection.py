import psycopg2
from LandInfo import LandInfo

columns = LandInfo()


class DbConnect:
    def __init__(self):
        self.connection = psycopg2.connect(
            "host=localhost port=5432 dbname=postgres user=postgres password=postgres"
        )
        self.cursor = self.connection.cursor()

    def db_select_all(self, table):
        sql = "SELECT * FROM " + table
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)

    def db_insert(self, table, list):
        sql = "INSERT INTO " + table + "(" + columns.columns_list + ") VALUES(%s, %s, %s, %s)"
        self.cursor.execute(sql, (list[0], list[1], list[2], list[3]))

    def db_rollback(self):
        print("rollback")
        self.connection.rollback()

    def db_commit(self):
        print("commit")
        self.connection.commit()

    def db_close(self):
        self.connection.close()
