from data_utils import load_data, save_data, ai_input, user_input_to_data
from emoji_library import emojis, display_emojis_tab
from clr_library import colors, display_clr_tab
from random import choice, randint
import json
import sys


def start_program(file_path="data.json"):
    display_items = False

    if input("\nDisplay items? [y/n] ").lower().startswith("y"):
        display_items = True

    data, data_keys = load_data(display_items, file_path)

    while True:
        user = input("\nMain ingredients: ")
        # leave 'False' as it is; (it's for test purposes)
        result = ai_input(data_keys, user, capitalized=True, test_on=False, threshold=60)

        if not result:
            pass
        # if theres any result from ai_input then take its 2nd element
        # data is a dictionary of the JSON file
        else:
            print(user_input_to_data(result[1], data))
            if input("\nContinue? [y/n] ").lower().startswith("y"):
                continue
            else:
                print("\nBon appétit!")
                break


def add_item(file_path="data.json"):
    """
    This function adds the new item to the dataset.
    """
    emoji_list = [_ for _ in emojis] # the list of emoji keys
    color_list = [_ for _ in colors]
    data, data_keys = load_data(False, file_path)
    new_ingr = {} # the root of the dictionary

    while True:
        ingr_name = input("\nThe main ingredient name: ").title()
        if ingr_name != "":
            if ingr_name not in data_keys:
                new_ingr[ingr_name] = {} # the main ingr name
                break
            else:
                print("Name already in a dataset.")
        else:
            print("Invalid Input. It can not be an empty string.")
            continue

    display_emojis_tab()

    while True:
        ingr_emo = input("The main ingredient emoji: ").lower()

        if ingr_emo != "":
            result = ai_input(emoji_list, ingr_emo, capitalized=False, test_on=False, threshold=60)
            if result:
                correct_emoji = result[1][0] # result = (Bool, ['correct_word'])
                new_ingr[ingr_name]["emoji"] = emojis[correct_emoji] # the main ingredient's emoji
                break
        else:
            print("Invalid Input. It can not be an empty string.")
            continue

    display_clr_tab() # displays a colorful table of colors

    while True:
        ingr_clr = input("The main ingredient color: ").lower()

        if ingr_clr != "":
            result = ai_input(color_list, ingr_clr, capitalized=False, test_on=False, threshold=60)
            if result:
                correct_color = result[1][0]
                new_ingr[ingr_name]["color"] = colors[correct_color] # the main ingredient's color
                break
        else:
            print("Invalid Input. It can not be an empty string.")
            continue


    while True:
        sub_ingr_name = input("Sub ingredient name: ").lower()

        if sub_ingr_name != "":
            new_data = {}

            sub_ingr_note = input("Sub ingredient note: ").lower()
            new_data["note"] = sub_ingr_note
            display_emojis_tab()
            while True:
                sub_ingr_emoji = input("Sub ingredient emoji: ").lower()
                if sub_ingr_emoji != "":
                    result = ai_input(emoji_list, sub_ingr_emoji, capitalized=False, test_on=False, threshold=60)
                    if result:
                        correct_emoji = result[1][0] # result = (Bool, ['correct_word'])
                        new_data["emoji"] = emojis[correct_emoji]
                        break
                    else:
                        continue
                else:
                    print("Invalid Input. It can not be an empty string.")
                    continue

            display_clr_tab() # displays a colorful table of colors

            while True:
                sub_ingr_color = input("Sub ingredient color: ").lower()
                if sub_ingr_color != "":
                    result = ai_input(color_list, sub_ingr_color, capitalized=False, test_on=False, threshold=60)
                    if result:
                        correct_color_name = result[1][0]
                        new_data["color"] = colors[correct_color_name]
                        break
                else:
                    print("Invalid Input. It can not be an empty string.")
                    continue

            new_ingr[ingr_name][sub_ingr_name] = new_data # the main ingredient's sub ingr

            if input("Would you like to add more sub ingredients? [y/n] ").lower()[0]=="y":
                continue
            else:
                break

        else:
            print("Invalid Input. It can\'t be an empty string.")
            continue

    save_data(new_ingr)


def remove_item(file_path="data.json"):
    print("Removing Assistant")
    while True:
        var = input("Display items? [y/n] ").lower()[0]
        if var=="y":
            display_on = True
            break
        elif var=="n":
            display_on = False
            break
        else:
            print("Invalid Input. Choose y/n. ")
            continue

    # load the current data
    data, data_keys = load_data(display_on, file_path)

    while True:

        user_remove_item = input("Choose item to remove: ")
        while True:
            try:
                suggestion = ai_input(data_keys, user_remove_item, capitalized=True, test_on=False, threshold=60)
                break
            except IndexError:
                print("Wrong input. Try again.")
                continue

        if suggestion:
            for name in suggestion[1]:

                if name in data:
                    data.pop(name)
                    print(f"Removed '{name}' from the JSON file.")
                else:
                    print(f"The '{name}' not found in the JSON file.")

            with open(file_path, "w") as data_file:
                json.dump(data, data_file, indent=4)
            break

        else:
            print("No match. Try again.")
            continue


def surprise_me(file_path):
    print("Not ready yet")
    data, data_keys = load_data(False, file_path)
    # find from 2 to 5 random items and rem. duplicates
    temp_list = list(set([choice(data_keys) for x in range(randint(2,5))]))
    # print(temp_list)
    for i in range(0, len(temp_list)):
        if i+1 < len(temp_list):
            for n in temp_list[i: i+2]:
                print(n, list(data[n].keys())[2:])
        print("")
        # print(list(data[i].keys())[2:])


def exit_program():
    print("Exiting program...")
    sys.exit()
