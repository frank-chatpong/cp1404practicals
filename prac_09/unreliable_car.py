"""
CP1404/CP5632 Practical - unreliable car program.
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent a Car that only sometimes successfully drives."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance.

        name: string, car's name
        fuel: float, one unit of fuel drives one kilometre
        reliability: float between 0 and 100"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car a given distance with reliability result."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return 0
