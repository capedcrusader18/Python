import pymysql

host="localhost"
user="root"
password="jarvis1897"

conn=pymysql.connect(host=host, user=user,password=password)

cur=conn.cursor()

cur.execute("CREATE DATABASE DEMO")

cur.execute("SHOW DATABASES")

databaselist=cur.fetchall()

for database in databaselist:
    print(database)


conn.close()