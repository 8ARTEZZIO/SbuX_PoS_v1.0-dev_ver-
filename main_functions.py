"""
This module contains the main functions of the program.
"""
import sys
from random import choice, randint
from data_utils import load_data, ai_input, display_data

try:
    from colorama import Style, init
except ModuleNotFoundError:  # pragma: no cover - fallback when colorama is missing
    class Style:  # type: ignore
        RESET_ALL = ""

    def init() -> None:  # type: ignore
        return None
else:
    init()

def start(file_path):
    """
    Starts a program and allows to search for items.
    """
    data = load_data(file_path)
    data_keys = list(data.keys())
    display_data(data_keys)

    res = []
    while True:

        user = input("\nWhat category: ")
        if user == "":
            print("Invalid Input. It can not be an empty string.")
            continue
        # leave 'False' as it is; (it's for test purposes)
        result = ai_input(data_keys, user, True, False, 60)
        if not result:
            pass
        display_data(list(data[result[0]].keys()))

        user_two = input("\nWhat drink: ")
        if user_two == "":
            print("Invalid Input. It can not be an empty string.")
            continue
        result_two = ai_input(list(data[result[0]].keys()), user_two, True, False, 60)
        if not result_two:
            pass
        res.extend([result[0], result_two[0], list(data[result[0]][result_two[0]].keys())[3:]])

        # if theres any result from ai_input then take its 2nd element
        # data is a dictionary of the JSON file
        if len(res) == 3:
            print(iterate_data(res, data))
        if input("\nContinue? [y/n] ").lower().startswith("y"):
            display_data(data_keys)
            res = []
            continue
        print("\nBon appétit!")
        break


def iterate_data(user, data):
    """
    user - the closest matches of ingredients to user's input
    data - dictionary of the JSON file (ingredients_data in this specific case)
    """

    message = ""

    word = user
    data_keys = list(data[word[0]][word[1]].keys())[3:]
    display_data(data_keys)
    while True:
        user = input("\nChoose additional: ")
        if user == "":
            print("Invalid Input. It can not be an empty string.")
            continue
        result = ai_input(data_keys, user, False, False, 60)

        if result:
            break

        continue

    color = data[word[0]][word[1]]["color"]
    note = data[word[0]][word[1]]["note"]
    emoji = data[word[0]][word[1]]["emoji"]

    message += f"\n{color}{word[1]}{Style.RESET_ALL} {emoji} | {note}\n"

    # TODO: # iterate over the sub ingredients if they exist in the data

    if word[2]:
        message += "Additions:\n"
        for w in result:
            add_list = []
            note = data[word[0]][word[1]][w]["note"]
            emoji = data[word[0]][word[1]][w]["emoji"]
            color = data[word[0]][word[1]][w]["color"]
            add_list.append(f"\t{color}{w}{Style.RESET_ALL} {emoji} | {note}\n")
            message += "".join(add_list)
    return message


# TODO: work on a function that generates a random combination of items
def rand(file_path):
    """
    Generates a random combination of items.
    """
    print("Not ready yet")
    data, data_keys = load_data(file_path)
    # find from 2 to 5 random items and rem. duplicates
    temp_list = list({choice(data_keys) for x in range(randint(2,5))})
    # print(temp_list)
    for i in range(0, len(temp_list)):
        if i+1 < len(temp_list):
            for n in temp_list[i: i+2]:
                print(n, list(data[n].keys())[2:])
        print("")
        # print(list(data[i].keys())[2:])


def ext_program(file_path):
    """
    Exits the program.
    """
    print("Exiting program...")
    sys.exit()
