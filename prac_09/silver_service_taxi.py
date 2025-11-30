"""CP1404/CP5632 Practical - SilverServiceTaxi class"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi, based on parent Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Get fare included flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string included flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
