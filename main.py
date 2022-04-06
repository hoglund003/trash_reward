import time

class Trash:
    def __init__(self, _weight, _distance_to_point):
        self.weight = _weight
        self.distance_to_point = _distance_to_point

        self.points = _weight * _distance_to_point / 100

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

        delivery = Trash(int(amount), int(distance))
        print(f"Your points: {delivery.points}")

        time.sleep(2)
