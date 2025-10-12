"""
CP1404/CP5632 Practical
Quick picks program in practical 04
"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate random quick pick numbers."""
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join(f"{number:2}" for number in quick_pick))


main()