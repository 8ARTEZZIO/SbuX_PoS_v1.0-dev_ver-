from colorama import Fore, Style
from tabulate import tabulate # type: ignore

# All accessible colors in colorama and additional colors from the provided database
colors = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "light_black": Fore.LIGHTBLACK_EX,
    "light_red": Fore.LIGHTRED_EX,
    "light_green": Fore.LIGHTGREEN_EX,
    "light_yellow": Fore.LIGHTYELLOW_EX,
    "light_blue": Fore.LIGHTBLUE_EX,
    "light_magenta": Fore.LIGHTMAGENTA_EX,
    "light_cyan": Fore.LIGHTCYAN_EX,
    "light_white": Fore.LIGHTWHITE_EX,
    "reset": Style.RESET_ALL,  # To reset formatting
    # Custom hex values from the provided database
    "\u001b[30m": "black",
    "\u001b[31m": "red",
    "\u001b[32m": "green",
    "\u001b[33m": "yellow",
    "\u001b[34m": "blue",
    "\u001b[35m": "magenta",
    "\u001b[36m": "cyan",
    "\u001b[37m": "white",
    "\u001b[90m": "light_black",
    "\u001b[91m": "light_red",
    "\u001b[92m": "light_green",
    "\u001b[93m": "light_yellow",
    "\u001b[94m": "light_blue",
    "\u001b[95m": "light_magenta",
    "\u001b[96m": "light_cyan",
    "\u001b[97m": "light_white",
}

def display_clr_tab():
    colors_names_list = []

    for name in colors:
        if "\u001b" not in name and name != "reset":
            if "_" in name:
                new_name = name.replace("_", " ")
                colors_names_list.append(colors[name] + new_name + Style.RESET_ALL)
            else:
                colors_names_list.append(colors[name] + name + Style.RESET_ALL)

    # table = [[c for c in colors_names_list[i:i+5]] for i in range(0, len(colors_names_list), 5)]

    table = []
    for i in range(0, len(colors_names_list), 5):
        row = []
        for c in colors_names_list[i:i+5]:
            row.append(c)
        table.append(row)

    print(tabulate(table, tablefmt="fancy_grid"))
