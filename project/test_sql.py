# select data which joined table result from postgres database

import psycopg2

class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host=' ', dbname=' ',user='',password='',port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()
        
        
if __name__=="__main__":
    db = Databases()
    print("first api")
    query1 = """""
    
    row = db.execute(query1)
    print(row)