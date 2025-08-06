"""
This module contains functions that are used to load, save and process data.
"""
import re
import json
from rapidfuzz import fuzz, process  # type: ignore
from tabulate import tabulate  # type: ignore

try:
    from colorama import Fore, Style, init
except ModuleNotFoundError:  # pragma: no cover - fallback when colorama is missing
    class Fore:  # type: ignore
        GREEN = ""

    class Style:  # type: ignore
        RESET_ALL = ""

    def init() -> None:  # type: ignore
        """Compatibility stub when colorama is unavailable."""
        return None
else:
    init()


def load_data(file_path):
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
            json.dump(data, data_file, indent=4)

    return data


def display_data(data_keys):
    """
    Displays the data in a table format
    """
    table = []

    for i in range(0, len(data_keys), 4):
        row = [Fore.GREEN + item + Style.RESET_ALL for item in data_keys[i: i+4]]
        table.append(row)

    print(tabulate(table, tablefmt="fancy_grid"))


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
            rslt = process.extract(word, choices, limit=3)
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
                l = str(len(close_matches))
                prompt = "Choose max " + l + f" [{s}]:\n" + "\n".join(close_matches) + "\n"
                user_input_close_matches = input(prompt)

                if "n" not in user_input_close_matches: # avoid casting a letter 'n' to integer
                    u = [int(i) for i in user_input_close_matches]

                    if len(u) == 1 and str(u[0]) in s:
                        return [close_matches[u[0]-1]]

                    if all((isinstance(x, int) for x in u if str(x) in s)) and len(u) <= 3:

                        nums = []
                        for i in list(u):
                            nums.append(int(i))

                        ret = []
                        for n in nums:

                            ret.append(close_matches[n-1])

                        return ret
                return []

    # avoid outputting the empty string
    if correct_words:

        if not test_on:
            intel_msg = f"\nDid you mean '{', '.join(correct_words)}'? [y/n] "
            if input(intel_msg).lower().startswith("y"):
                return correct_words
            return []
        # this part of code runs only while testing is ON (test_on==True)
        return correct_words
