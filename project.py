from main_functions import start_program, add_item, remove_item, exit_program, surprise_me

FILE_PATH = "starbucks_data.json" # choose a dataset to read from

def main():
    """
    The main interface that allows graceful dealing with the codebase.
    It allows to start program, add an item and exit.
    """
    menu_options = {
        "s" : start_program,
        "a" : add_item,
        "r" : remove_item,
        "*" : surprise_me,
        "e" : exit_program
    }

    while True:
        print("Options: ")
        print("[s] start program")
        print("[a / r] add / remove item")
        print("[*] random combination")
        print("[e] exit program")

        try:
            var = input("").lower()[0]
        except IndexError:
            print("Invalid Input. Type in the correct letter from av. options.")

        if var in menu_options:
            menu_options[var](file_path=FILE_PATH)
        else:
            print("Invalid input. Please choose [s|a|r|*|e].")


if __name__ == "__main__":
    main()
