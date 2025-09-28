"""
CP1404/CP5632 - Practical
Program to get score, print result, show stars
"""

MENU = """(G)et a valid score
(P)rint result 
(S)how stars 
(Q)uit"""


def main():
    """Score menu program"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Your score is {score}")
        elif choice == "P":
            print(f"Your grade: {determine_grade(score)}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """Check valid score"""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score! (must be 0-100 inclusive)")
        score = float(input("Score: "))
    return score


def determine_grade(score):
    """Determine grade by score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print as many stars as the score."""
    print('*' * int(score))


main()
