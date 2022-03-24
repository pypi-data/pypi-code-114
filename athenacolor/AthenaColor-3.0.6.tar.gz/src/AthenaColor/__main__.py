# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Help.readme import readme

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    readme()


    from AthenaColor.Styling.Callable import (
        Fore, Back, Style
    )

    print(
        Fore.Blue(
            "blue",
            Fore.Red("red"),
            Back.Crimson("something"),
            Style.Bold("PLEASE HELP ME"),
            Style.Underline("HERE"),
            "blue",
            Fore.Red("red"),
        )
    )

    print(
        Style.Bold(
            "BOLD",
            Style.Bold("BOLD"),
            "BOLD"
        ),
        "not"
    )
