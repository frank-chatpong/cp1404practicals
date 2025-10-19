"""
Emails
Estimate: 20 minutes
Actual:  16  minutes
"""


def main():
    """Create dictionary of email to name"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n) ")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract a name from the email address."""
    name_part = email.split('@')[0]
    parts = name_part.split('.')
    name = ' '.join(parts).title()
    return name


main()
