"""
Description: 
The main interface that allows graceful dealing with the codebase.
"""
from main_functions import start, ext_program

FILE_PATH = "starbucks_data.json"  # choose a dataset to read from


def main():
    """
    It allows to start program, add an item and exit etc.
    """
    menu_options = {
        "s": start,
        # "r": rand,
        "e": ext_program
    }

    while True:
        print("Options: ")
        print("[s] start program")
        # TODO : implement random combination
        # print("[r] random combination")
        print("[e] exit program")

        try:
            var = input("").lower()[0]
        except IndexError:
            print("Invalid input. Please choose [s|e].")
            continue

        if var in menu_options:
            menu_options[var](file_path=FILE_PATH)
        else:
            print("Invalid input. Please choose [s|e].")


if __name__ == "__main__":
    main()
