"""Test suite for Starbucks POS helper functions."""

from data_utils import load_data
from main_functions import iterate_data


def test_load_data():
    """Ensure JSON data is loaded into a dictionary with expected keys."""
    data = load_data("starbucks_data.json")
    assert isinstance(data, dict)
    assert "Coffee And Espresso" in data


def test_iterate_data(monkeypatch):
    """`iterate_data` should include the chosen addition in the output message."""
    data = load_data("starbucks_data.json")
    user_choice = [
        "Coffee And Espresso",
        "Espresso Roast",
        ["chocolate", "vanilla", "hazelnut"],
    ]

    # Simulate user selecting "chocolate" and confirming the suggestion
    inputs = iter(["chocolate", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    message = iterate_data(user_choice, data)
    assert "Espresso Roast" in message
    assert "chocolate" in message
    assert "Additions" in message

