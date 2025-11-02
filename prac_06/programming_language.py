"""
CP1404/CP5632 Practical - ProgrammingLanguage class example.
Estimate: 20 minutes
Actual:    minutes
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage from the given values

        name: language name
        typing: Static or Dynamic
        reflection: True if it can do reflection
        year: starting year
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year





