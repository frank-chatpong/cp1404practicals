"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display"""
    subject_data = load_subjects(FILENAME)
    display_subjects(subject_data)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students.
    Return data as a list of [subject, lecturer, number_of_students].
    """
    subject_data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)  # Add this list to the data list
    input_file.close()  # Close the file
    return subject_data


def display_subjects(subject_data):
    """Display subject, lecturer, and number_of_students from the subject data list."""
    for subject, lecturer, number_of_students in subject_data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students")


main()

