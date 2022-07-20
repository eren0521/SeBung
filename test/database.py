import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1", user="root", password="0521", db="pro", charset="utf8", port=3306)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query):
        self.cursor.execute(query)

    def execute_one(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        return row

    def execute_all(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()