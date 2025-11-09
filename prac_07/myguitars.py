"""
CP1404/CP5632 Practical
Read guitars from a CSV file, store as Guitar objects, and display them sorted by year.
"""

from prac_07.guitar import Guitar
import csv


def main():
    """Read CSV file and display guitars sorted by year."""
    guitars = load_guitars("guitars.csv")
    print("All guitar")
    for guitar in guitars:
        print(guitar)

    add_new_guitars(guitars)

    guitars.sort()

    print("\nSorted Guitars (oldest to newest):")
    for guitar in guitars:
        vintage_label = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage_label}")


def load_guitars(filename):
    """Load guitars from CSV file and return list of Guitar objects."""
    guitars = []
    in_file = open(filename, "r")
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars

def add_new_guitars(guitars):
    """Ask user to add new guitar to the list."""
    print("\nAdd new guitars (leave it blank to finish):")
    name = input("Name: ").strip()
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input! Please enter number for year and cost.")
        else:
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar} added.")
        name = input("Name: ").strip()


main()
