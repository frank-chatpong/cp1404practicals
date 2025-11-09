"""
CP1404/CP5632 Practical
Read guitars from a CSV file, store as Guitar objects, and display them sorted by year.
"""

from prac_07.guitar import Guitar
import csv


def main():
    """Read CSV file and display guitars sorted by year."""
    guitars = load_guitars("guitars.csv")


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
