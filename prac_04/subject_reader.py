"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students.
    Return data as a list of [subject, lecturer, number_of_students].
    """
    data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()              # Remove the \n
        parts = line.split(',')          # Separate the data into its parts
        parts[2] = int(parts[2])         # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)               # Add this list to the data list
    input_file.close()                   # Close the file
    return data


main()
