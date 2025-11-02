"""
Estimate: 20 minutes
Actual:    minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Testing class ProgrammingLanguage."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, "1995")
    c_plus_plus = ProgrammingLanguage("C++", "Static", True, "1983")
    print(python)

    languages = [python, ruby, visual_basic, java, c_plus_plus]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
