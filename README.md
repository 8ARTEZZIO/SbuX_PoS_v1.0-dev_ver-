# STARBUCKS POS

## Video Demo
[Watch the Demo on YouTube](https://www.youtube.com/watch?v=vpb18Lalnvc)

## Description
Ever wondered about becoming a professional barista? While this tool might not make you one overnight, it will get you closer to crafting incredible drink combinations! 

The program allows users to explore and combine ingredients to create drinks. Tested and proven in real life, this tool is perfect for unleashing your inner barista.

## Features
- **Ingredient Matching**: Input ingredients and find perfect matches.
- **Taste Notes**: Gain insights into the predicted flavor profiles.
- **Interactive User Interface**: Use the terminal to navigate and select options effortlessly.
- **Dynamic Suggestions**: Handles misspellings and offers close matches.

## Quick Start

### 1. Setup the Environment
Install the required dependencies:
```bash
pip install rapidfuzz tabulate wcwidth
```
Alternatively, install from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 2. Prepare Data
The tool uses a JSON file (`starbucks_data.json`) as its data source. If the file doesn't exist, the program generates it automatically with example data.

### 3. Run the Program
Launch the script using Python:
```bash
python project.py
```

### 4. Explore Features
- Input ingredient categories and names (e.g., **Espresso Roast**, **Vanilla Syrup**).
- Receive suggestions and taste profiles based on the combinations you choose.

## Key Functions

### `main()`
- The central loop that handles user input and navigates through the program options.

### `load_data()`
- Reads ingredients from `starbucks_data.json`. If the file is missing, it creates one with default data.

### `ai_input()`
- Takes user input and provides closest matches for ingredients.
- Ensures valid input through intelligent suggestions.

### `start()`
- Displays available ingredients and allows users to select and explore combinations.

### `iterate_data()`
- Processes user-selected ingredients and outputs detailed flavor profiles, including emojis and color-coded notes.

## Customization
You can easily modify the ingredient data:
1. Open `starbucks_data.json`.
2. Add or edit ingredients, taste notes, and pairings.
3. Save the file and relaunch the program.

## Testing
Run tests using `test_project.py` to validate the core functions:
```bash
pytest -s test_project.py
```
Focus on edge cases, such as misspelled inputs and invalid JSON structures.

## Future Improvements
- Implement the `rand()` function to suggest random ingredient combinations.
- Add support for custom taste profiles and additional ingredient categories.

## Contribution
1. Clone the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

## Dependencies
- `rapidfuzz`: For fast string matching.
- `tabulate`: For displaying data in table formats.
- `wcwidth`: For managing string widths, including emojis.

---

Start your barista adventure today with **Starbucks POS**!
