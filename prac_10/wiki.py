"""

"""

import wikipedia


def main():
    """Run the Wikipedia search loop until the user enters blank input."""
    wikipedia.set_lang("en")
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title)
        except wikipedia.DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)
        except wikipedia.PageError as error:
            print(error)
        else:
            print_page_info(page)

        print()
        title = input("Enter page title: ").strip()

 


