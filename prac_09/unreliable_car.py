"""
CP1404/CP5632 Practical - unreliable car program.
"""
import random
from car import Car

class UnriliableCar:
    """Represent a Car that only sometimes successfully drives."""
    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance.

        name: string, car's name
        fuel: float, one unit of fuel drives one kilometre
        reliability: float between 0 and 100"""
        super().__init__(name, fuel)
        self.reliability = reliability



