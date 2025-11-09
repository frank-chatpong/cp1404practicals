"""
CP1404/CP5632 Practical
Project program
Estimate: 60 minutes
Actual:    minutes
"""

import datetime

DATE_FORMAT = "%d/%m/%Y"
FIELD_SEPERATOR = "\t"

class Project:
    """Represent a project entry."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Allow sorting by priority (lower number = higher priority)."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if project is completed."""
        return self.completion_percentage >= 100



