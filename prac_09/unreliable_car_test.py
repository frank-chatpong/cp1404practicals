"""
CP1404/CP5632 Practical - Client code to use the Car and UnreliableCar class.
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Demo test code to show how to use UnreliableCar class."""
    reliable_car = UnreliableCar("Good car", 100, 90)
    unreliable_car = UnreliableCar("Bad car", 100, 10)

    for i in range(1, 30):
        print(f"Attempting to drive {i} km.")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2} km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive:2} km")
    print(reliable_car)
    print(unreliable_car)


main()
