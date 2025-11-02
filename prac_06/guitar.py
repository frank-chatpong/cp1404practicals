"""
CP1404/CP5632 Practical - Guitar program.
Estimate: 30 minutes
Actual:    minutes
"""
CURRENT_YEAR = 2025


class Guitar:
    """Represent a Guitar objects."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, guitar's name
        year: int, the year that guitar is made
        cost: float, guitar's price
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns how old the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= 50


