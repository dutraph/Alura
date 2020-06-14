import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pa123ulo'
)

print(mydb)