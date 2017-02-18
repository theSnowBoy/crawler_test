#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='wang',
        passwd='123',
        db ='test',
        )
cur = conn.cursor()
cur.execute("insert test_1(data) values('hello mysql')")

cur.close()
conn.commit()
conn.close()