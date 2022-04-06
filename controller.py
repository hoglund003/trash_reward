import time
import mysql.connector
import secrets_file
from tabulate import tabulate

database = mysql.connector.connect(
    host=secrets_file.DB_IP_ADDRESS,
    user=secrets_file.DB_USERNAME,
    password=secrets_file.DB_PASSWD,
    database="trash_reward"
)

cursor = database.cursor()
class Trash:
    def __init__(self, _weight, _distance_to_point, _plucker_id):
        self.weight = _weight
        self.distance_to_point = _distance_to_point
        self.plucker_id = _plucker_id

        self.points = _weight * _distance_to_point / 100

def validate_id(id):
    cursor.execute(f"SELECT points FROM pluckers WHERE id = {id}")
    points = cursor.fetchone()
    if points == None:
        print("Plucker could not be found :(")
        return False
    else:
        return float(''.join(map(str, points)))

def read_points(plucker_id):
    if not validate_id(plucker_id) == False:
        return validate_id(plucker_id)

def append_to_points(plucker_id, total_points):
    if validate_id(plucker_id):
        cursor.execute(f"UPDATE pluckers SET points = {total_points} WHERE id = {plucker_id}")
        database.commit()

def get_all_pluckers():
    cursor.execute("SELECT * FROM pluckers ORDER BY points DESC")
    pluckers = cursor.fetchall()

    return pluckers




