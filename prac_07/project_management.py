"""
CP1404/CP5632 Practical
project management program
Main program for managing a list of projects.
"""

import datetime
from project import Project

PROJECT_FILE = "projects.txt"
FIELD_SEPARATOR = "\t"

MENU = (
    "- (L)oad projects  \n"
    "- (S)ave projects  \n"
    "- (D)isplay projects  \n"
    "- (F)ilter projects by date\n"
    "- (A)dd new project  \n"
    "- (U)pdate project\n"
    "- (Q)uit\n"
    ">>> "
)

def main():
    print("Welcome to Pythonic Project Management")


def convert_to_date(date_text)
    """Convert a string like 'dd/mm/yyyy' or 'dd/mm/yy' into a date object."""
    date_text = date_text.strip()
    for i in ("%d/%m/%Y", "%d/%m/%y"):
        try:
            return datetime.datetime.strptime(date_text, i).date()
        except ValueError:
            print(end="")
    print(f"Invalid date format: {date_text} (use dd/mm/yy or dd/mm/yyyy)")
    return None

def load_projects(filename):
    """Load projects from file and return a new list."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            if line.strip():
                project = create_project_from_row(line)
                if project is not None:
                    projects.append(project)
    return projects
