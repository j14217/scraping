import psycopg2

class DbConnect:
    def __init__(self):
        self.connection = psycopg2.connect(
            "host=192.168.0.109 port=5432 dbname=postgres user=postgres password=scrapingland"
        )
        self.cursor = self.connection.cursor()

    def db_select_all(self, table):
        sql = "SELECT * FROM " + table
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)

    def db_insert_test(self, table, columns, info_tuple):
        sql = "INSERT INTO " + table + " (" + columns + ") VALUES(%s, %s, %s, %s)"
        self.cursor.execute(sql, info_tuple)

    def db_insert1(self, table, columns, info_tuple):
        sql = "INSERT INTO " + table + " (" + columns + ") VALUES("\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s"\
            ")"
        self.cursor.execute(sql, info_tuple)

    def db_insert2(self, table, columns, info_tuple):
        sql = "INSERT INTO " + table + "(" + columns + ") VALUES("\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s,"\
            "%s, %s, %s, %s, %s"\
            "%s, %s"\
            ")"
        self.cursor.execute(sql, info_tuple)

    def db_rollback(self):
        print("rollback")
        self.connection.rollback()

    def db_commit(self):
        print("commit")
        self.connection.commit()

    def db_close(self):
        self.connection.close()