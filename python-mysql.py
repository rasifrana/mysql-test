import os
import pymysql


username = os.getenv("root")

# Connection
connection = pymysql.connect(host="localhost",
                            user=username,
                            password="",
                            db="Chinook")

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist limit 5;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()