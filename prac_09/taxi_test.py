"""
CP1404/CP5632 Practical - Client code to use the Car and Taxi class.
"""

from prac_09.taxi import Taxi


def main():
    """Demo test code to show how to use Taxi class."""
    # my_taxi = Taxi("Prius 1", 100, 1.23)
    # my_taxi.drive(40)
    # print(my_taxi)
    # my_taxi.start_fare()
    # my_taxi.drive(100)
    # print(my_taxi)

    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    print(
        f"{my_taxi.name} has fuel: {my_taxi.fuel} and driven: {my_taxi.current_fare_distance}km, "
        f"the current fare: {my_taxi.get_fare()}")

    print("<<<Restart meter>>>")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"{my_taxi.name} has fuel: {my_taxi.fuel} and driven: {my_taxi.current_fare_distance}km,"
          f"the current fare: {my_taxi.get_fare()}")


main()
