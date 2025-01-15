"""
This module contains a dictionary of colors 
that can be used to display text in different colors.
"""
from colorama import Fore

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
}
