import time
import os

path = "points.txt"

class Trash:
    def __init__(self, _weight, _distance_to_point):
        self.weight = _weight
        self.distance_to_point = _distance_to_point

        self.points = _weight * _distance_to_point / 100

def read_points():
    if os.path.exists(path):
        with open('points.txt', 'r') as file:
            points = file.readline()
            return float(points)
    else:
        return 0

def append_to_points(total_points):
    with open('points.txt', 'w+') as file:
        file.write(str(total_points))

while True:
    print("--------TRASH REWARD!!-------")
    print("Deliver trash...............[1]")
    print("Enter choice: ", end="")
    choice = input()

    if choice == "1":
        print("Kilos of trash: ", end="")
        amount = input()
        print("Meters from trash pickup point to delivery point: ", end="")
        distance = input()

        delivery = Trash(float(amount), float(distance))
        total_points = read_points() + delivery.points
        append_to_points(total_points)

        print(f"Your points: {total_points}")

        time.sleep(2)
