"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

"""
Questions

1. When will a ValueError occur?
ANS : The ValueError occur when the input is not int.
2. When will a ZeroDivisionError occur?
ANS : The ZeroDivisionError occur when the user try to divide by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
ANS : yes 

"""