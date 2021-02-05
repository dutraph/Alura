from logging import error
import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host='localhost', user='root', password='pa123ulo', database='bd')
    print("Conexao feita...")

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database nao existe!")

    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario ou senha errada")
    else:
        print(error)
else:
	db_connection.close()

