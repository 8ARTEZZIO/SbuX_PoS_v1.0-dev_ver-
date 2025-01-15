"""
This file contains the test functions for the functions in the main_functions.py file
"""
from data_utils import load_data
from main_functions import iterate_data

data = load_data("starbucks_data.json")
ingredient_names = list(data.keys())

def test_load_data():
    """
    Test the load_data function
    """
    assert load_data("starbucks_data.json") == data
    assert load_data("starbucks_data.json") != {}


def iterate_data_test():
    """
    Test the iterate_data function
    """
    assert iterate_data(["Coffee And Espresso", "Espresso Roast", ["chocolate", "vanilla", "hazelnut"]], data) == "milk, coffee, sugar"
