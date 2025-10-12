"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display"""
    data = load_subjects(FILENAME)
    display_subjects(data)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students.
    Return data as a list of [subject, lecturer, number_of_students].
    """
    data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)  # Add this list to the data list
    input_file.close()  # Close the file
    return data


def display_subjects(data):
    """Display subject, lecturer, and number_of_students from the data list."""
    for subject, lecturer, number_of_students in data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students")


main()
