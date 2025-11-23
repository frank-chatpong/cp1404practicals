"""CP1404/CP5632 Practical - Test SilverServiceTaxi class"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    test_taxi.start_fare()
    test_taxi.drive(18)
    fare = test_taxi.get_fare()
    print(test_taxi)
    print(fare)


main()
