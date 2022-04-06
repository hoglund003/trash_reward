import time
import mysql.connector
import secrets
from tabulate import tabulate

database = mysql.connector.connect(
    host=secrets.DB_IP_ADDRESS,
    user=secrets.DB_USERNAME,
    password=secrets.DB_PASSWD,
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

while True:
    print("--------TRASH REWARD!!-------")
    print("Deliver trash..............[1]")
    print("Get points from plucker....[2]")
    print("Show all pluckers..........[3]")
    print("Enter choice: ", end="")
    choice = input()

    if choice == "1":
        print("Your ID: ", end="")
        plucker_id = input()
        print("Kilos of trash: ", end="")
        amount = input()
        print("Meters from trash pickup point to delivery point: ", end="")
        distance = input()

        delivery = Trash(float(amount), float(distance), int(plucker_id))
        if validate_id(plucker_id):
            total_points = read_points(plucker_id) + delivery.points
            append_to_points(plucker_id, total_points)

        print(f"Your points: {total_points}")

        time.sleep(2)
    elif choice == "2":
        print("Pluckers ID: ", end="")
        plucker_id = input()
        points = read_points(plucker_id)
        if points:
            print(f"The plucker with ID {plucker_id}, has {points} points")

    elif choice == "3":
        sql = cursor.execute("SELECT * FROM pluckers ORDER BY points DESC")
        pluckers = cursor.fetchall()
        table = [["ID", "Points", "Date Created"]]

        for plucker in pluckers:
            table.append([plucker[0], plucker[1], plucker[2]])
        
        print(tabulate(table))


