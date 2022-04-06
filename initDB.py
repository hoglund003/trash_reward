import mysql.connector
import secrets


database = mysql.connector.connect(
    host=secrets.DB_IP_ADDRESS,
    user=secrets.DB_USERNAME,
    password=secrets.DB_PASSWD
)

cursor = database.cursor()
cursor.execute("CREATE DATABASE trash_reward")

database = mysql.connector.connect(
    host=secrets.DB_IP_ADDRESS,
    user=secrets.DB_USERNAME,
    password=secrets.DB_PASSWD,
    database="trash_reward"
)

cursor = database.cursor()
cursor.execute("CREATE TABLE pluckers (id  INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, points DECIMAL(10, 2), date_added DATETIME DEFAULT NOW())")
cursor.execute("INSERT INTO pluckers (points) VALUES (0.0);")
cursor.execute("INSERT INTO pluckers (points) VALUES (35.2);")
cursor.execute("INSERT INTO pluckers (points) VALUES (2.42);")
database.commit()