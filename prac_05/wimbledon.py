"""
CP1404/CP5632 Practical
Wimbledon
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read the file and show Wimbledon champions and countries."""
    records = read_file(FILENAME)
    champion_to_count, country_set = count_champions_and_countries(records)
    display_results(champion_to_count, country_set)


def read_file(filename):
    """Read CSV file and return data as a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        for line in file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


def count_champions_and_countries(records):
    """Make a dictionary for champions and a set for countries."""
    champion_count = {}
    country_set = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]
        country_set.add(country)
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count, country_set


def display_results(champion_count, country_set):
    """Print champions and countries nicely."""
    print("Wimbledon Champions:")
    for name, wins in sorted(champion_count.items()):
        print(f"{name:20} {wins}")

    print(f"\nThese {len(country_set)} countries have won Wimbledon:")
    print(", ".join(sorted(country_set)))


main()
