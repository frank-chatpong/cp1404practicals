MINIMUM_LENGTH = 10


def main():
    """Get password and print stars"""
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(min_length):
    """Get password that meets the required minimum length"""
    password = input(f"Please enter the password (at least {min_length} characters): ")
    while len(password) < min_length:
        print("Error: Password too short!")
        password = input(f"Please enter the password (at least {min_length} characters): ")
    return password


def print_stars(password):
    """Print stars as long as the password"""
    print('*' * len(password))


main()
