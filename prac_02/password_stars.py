MINIMUM_LENGTH = 10


def main():
    """Get password and print asterisks """
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(password_length):
    """Get password that meets the required length"""
    password = input(f"Please enter the password (at least {password_length} characters): ")
    while len(password) < password_length:
        print("Error: Password too short!")
        password = input(f"Please enter the password (at least {password_length} characters): ")
    return password


def print_asterisks(password):
    """Print asterisks as long as the password"""
    print('*' * len(password))


main()
