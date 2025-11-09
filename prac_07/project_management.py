"""
CP1404/CP5632 Practical
project management program
Main program for managing a list of projects.
"""

import datetime
from project import Project, DATE_FORMAT

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


def create_project_from_row(row):
    """Convert one line of text into a Project object."""
    parts = row.strip().split(FIELD_SEPARATOR)
    if len(parts) != 5:
        return ""

    name, start_text, priority_text, cost_text, percentage_text = parts
    start_date = convert_to_date(start_text)
    if start_date == "":
        return ""

    try:
        priority = int(priority_text)
        cost_estimate = float(cost_text)
        completion_percentage = int(percentage_text)
    except ValueError:
        return ""

    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def load_projects(filename):
    """Load projects from file and return a list of Project objects."""
    input_file = open(filename, "r")
    input_file.readline()  # ข้าม header
    project_list = []

    for line in input_file:
        if line.strip():
            project_object = create_project_from_row(line)
            if project_object != "":
                project_list.append(project_object)

    input_file.close()
    return project_list


def save_projects(filename, project_list):
    """Save all projects to a file."""
    output_file = open(filename, "w")
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)

    for project in project_list:
        print(
            f"{project.name}\t"
            f"{project.start_date.strftime(DATE_FORMAT)}\t"
            f"{project.priority}\t"
            f"{project.cost_estimate:.1f}\t"
            f"{project.completion_percentage}",
            file=output_file
        )

    output_file.close()

    def display_projects(project_list):
        """Display incomplete and completed projects."""
        incomplete_projects = sorted(
            [project for project in project_list if not project.is_complete()]
        )
        completed_projects = sorted(
            [project for project in project_list if project.is_complete()]
        )

        print("Incomplete projects:")
        for current_project in incomplete_projects:
            print(f"  {current_project.display_line()}")

        print("Completed projects:")
        for current_project in completed_projects:
            print(f"  {current_project.display_line()}")

    def filter_projects_by_date(project_list):
        """Show projects starting after a specific date."""
        date_text = input("Show projects that start after date (dd/mm/yy): ")
        filter_date = convert_to_date(date_text)
        filtered_projects = sorted(
            [project for project in project_list if project.start_date >= filter_date],
            key=lambda project: project.start_date
        )
        for current_project in filtered_projects:
            print(current_project.display_line())

    def add_new_project(project_list):
        """Add a new project to the list."""
        print("Let's add a new project")
        project_name = input("Name: ")
        date_text = input("Start date (dd/mm/yy): ")
        start_date = convert_to_date(date_text)
        project_priority = int(input("Priority: "))
        cost_text = input("Cost estimate: $").replace("$", "")
        project_cost = float(cost_text)
        completion_text = input("Percent complete: ")
        project_completion = int(completion_text)

        new_project = Project(project_name, start_date, project_priority, project_cost, project_completion)
        project_list.append(new_project)



