"""
CP1404/CP5632 Practical - Suggested Solution
Band class
"""


class Band:
    """Represent band that has musicians."""

    def __init__(self, name=""):
        """Initialize band"""
        self.name = name
        self.musician = []

    def __str__(self):
        """Return string of a band."""
        musician_strings = ", ".join(str(musician) for musician in self.musician)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add musician to the band."""
        self.musician.append(musician)

    def play(self):
        """Determine the instrument for musician"""
        return "\n".join(musician.play() for musician in self.musician)
