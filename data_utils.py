from colorama import Fore, Style, init
from rapidfuzz import fuzz, process # type: ignore
from tabulate import tabulate # type: ignore
import inflect # type: ignore
import re
import json
init()

def load_data(display_on, file_path):
    """
    Reads the data from a .json file
    Returns it as a dictionary
    """
    try:
        with open(file_path, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        data = {}
        with open(file_path, "w", encoding="utf-8") as data_file:
            data = json.dump(data, data_file, indent=4)

    # translate data into a list of keys
    data_keys = list(data.keys())

    if display_on:
        table = []

        for i in range(0, len(data_keys), 4):
            row = [Fore.GREEN + item + Style.RESET_ALL for item in data_keys[i: i+4]]
            table.append(row)

        print(tabulate(table, tablefmt="fancy_grid"))

    return data, data_keys


def save_data(new_data, file_path):
    try:
        with open(file_path, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open(file_path, "w") as data_file:
        json.dump(data, data_file, indent=4)


def ai_input(choices, user_input, capitalized, test_on, threshold=60):
    """
    Makes sure that user inputs the correct name
    Return (Bool, list)
    """
    # lower all the names of ingredients for flexibility
    choices = [x.lower() for x in choices]

    # clean the 'user_input' from all the empty strings
    user_input = [x for x in re.split(r"[;,.]+", user_input) if x != ""]

    correct_words = []
    close_matches = []

    for word in user_input:
        word = word.strip().lower()

        suggestion = process.extractOne(word, choices, scorer=fuzz.ratio)
        if suggestion and suggestion[1] > threshold:
            if capitalized:
                correct_words.append(suggestion[0].title())
            else:
                correct_words.append(suggestion[0])

        else:
            print("\nNo close match found.")

            threshold = 25
            # find closest 3 matches to the invalid input
            # use low threshold on a dataset
            LIMIT = 3
            rslt = process.extract(word, choices, limit=LIMIT)
            if rslt:
                for mtch in rslt:

                    if mtch[1] > threshold:
                        if capitalized:
                            close_matches.append(mtch[0].title())
                        else:
                            close_matches.append(mtch[0])
            # create an adjustable list of indexes e.g. "1/2/3/.../n"
            s = ""
            for i in range(len(close_matches)):
                s += str(i+1) + "\\"

            if close_matches:

                s = "\\".join(str(i + 1) for i in range(len(close_matches))) + "\\n"
                prompt = "Choose max " + str(len(close_matches)) + f" [{s}]:\n" + "\n".join(close_matches) + "\n"
                user_input_close_matches = input(prompt)

                if "n" not in user_input_close_matches: # avoid casting a letter 'n' to integer
                    u_inp = [int(i) for i in user_input_close_matches]

                    if len(u_inp) == 1 and str(u_inp[0]) in s:
                        return False, [close_matches[u_inp[0]-1]]
                    
                    elif all([isinstance(x, int) for x in u_inp if str(x) in s]) and len(u_inp) <= LIMIT:

                        nums = []
                        for i in list(u_inp):
                            nums.append(int(i))

                        ret = []
                        for n in nums:

                            ret.append(close_matches[n-1])

                        return False, ret
                else:
                    return []

    # avoid outputting the empty string
    if correct_words:

        if not test_on:
            intel_msg = f"\nDid you mean '{', '.join(correct_words)}'? [y/n] "
            if input(intel_msg).lower().startswith("y"):
                return True, correct_words
            else:
                return []
        # this part of code runs only while testing is ON (test_on==True)
        else:
            return correct_words


def user_input_to_data(user, data):
    """
    user - the closest matches of ingredients to user's input
    data - dictionary of the JSON file (ingredients_data in this specific case)

    Loads in the user's input and database
    Returns the ready output with ingredients
    """
    # simple check if data is a dictionary
    if isinstance(data, dict):
        p = inflect.engine()

        try:
            notes = []
            message = ""
            for chunk in user:

                ingredients = []
                for x in data[chunk]:

                    # add all the ingredients apart from emoji and color
                    if x not in ["emoji", "color"]:

                        ingredients.append(data[chunk][x]["color"] + x + Style.RESET_ALL)

                        for note in data[chunk][x]["note"].split(", "):
                            notes.append(note)

                mylist = p.join(ingredients, final_sep="")

                # use correct grammar
                if chunk[-1:] == 's':
                    message += f"\n{data[chunk]['color'] + chunk + Style.RESET_ALL + data[chunk]['emoji']}  compose well with:\n\t{mylist}\n"
                else:
                    message += f"\n{data[chunk]['color'] + chunk + Style.RESET_ALL + data[chunk]['emoji']}  composes well with:\n\t{mylist}\n"

            if notes:
                repeating_notes = {}

                for n in notes:
                    if n not in repeating_notes.keys():
                        repeating_notes[n] = 1
                    else:
                        repeating_notes[n] += 1

                # filter out the notes with repetition below 2
                filtered_notes = {k: v for k, v in repeating_notes.items() if v > 1}

                # sort all the filtered noted due to their values
                most_common = sorted(filtered_notes.items(), key=lambda x: x[1])[::-1]

                # present it in a form of a list
                final = [el[0] for el in most_common]

                # display the last msg ONLY if common notes found
                if final:
                    notes_info = p.join(final, final_sep="")
                    message += f"\nCommon notes in a mix of subingredients:\n\t{notes_info}"

            return message

        except KeyError:
            print('Invalid Main Ingredient')

    else:
        print("The user input is not a dict")
