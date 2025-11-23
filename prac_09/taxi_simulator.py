"""
CP1404/CP5632 Practical - Suggested Solution
Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n"

def main():
    """Demo texi simulator"""
    total_bill = 0
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    menu = "q)uit, c)hoose taxi, d)rive\n"
    choice = input(menu).lower()

    while choice != "q":
        if choice == "c":
            print("Taxis available:")

            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxi_choice
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi >= 0:
                distance = float(input("Drive how far? "))
                taxi = taxis[current_taxi]
                taxi.start_fare()
                taxi.drive(distance)
                trip_cost = taxi.get_fare()
                print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(menu).lower()

