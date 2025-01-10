# RESTAURANT'S CHEF BEST FRIEND
#### Video Demo: https://www.youtube.com/watch?v=rt3u0APaAYU
#### Description:
Have you ever thought about becoming a professional chef?
Well... maybe I can't help with that, but I can make you nearly as good as the real thing!

- **Run the program in a terminal.**
- Find some **interesting ingredients** and mix them with 1-2 of the proposed matches.
- Your outcome dish will most likely fall into the **predicted area of taste notes**.

This tool has been **tested in real life**, and it really works!
Unleash your inner chef and create something amazing today.

- **Choose any ingredients** you can see.
- **Mix and match** them to create intresting combination.
- Gain insights into the **likely taste notes**.

TO-DO List for New Developers:

1. **Understand the Project**
- Read the Code:
    Have a look on entire logic and structure.
- Understand the Use Case: The project helps users find the best ingredient combinations and predict taste notes.
- Dependencies: Libraries Used:
    - rapidfuzz
    - tabulate
    - wcwidth

2. **Setup the Environment**
- Install Dependencies: Use the following comand:
```bash
    pip install rapidfuzz tabulate wcwidth
    # or
    pip install -r requirements.txt
```
- Prepare <mark>data.json</mark>: If the file doesn't exist, the program generates it automatically using the example data.

3. Run the Program
- Run the Script: Open a terminal and execute the script:
```bash
python project.py
```
- Test the Features:
    - Use the provided ingredient names (e.g., **Strawberries**, **Apples**, etc.).
    - Experiment with different inputs to see how the program suggests matches and taste notes.

4. Understand the Key Functions
- <mark>main()</mark> : The main program loop. It handles the user input and (by using the functions below) displays the output.
- <mark>load_data()</mark> : Loads ingredients from JSON file or creates one if missing.
- <mark>ai_input()</mark> : Takes the available data of ingredients and users input. Finds the closest match to the provided string. Asks the user if it's the correct match. If it is - returns True and a list of corrected words.
- <mark>user_input_to_data()</mark> : Processes user input and formats the output with suggested combinations and taste notes.

5. Customize the Data
- Edit the <mark>ingredients_data</mark> :
    - Add new ingredients or taste pairings to make the tool more robust.
    - Save the Data:
        - Ensure updates to <mark>ingredients_data</mark> are saved in the <mark>data.json</mark> file.

6. Debugging and Testing
- Test Edge Cases:
    - Test with mispelled ingredient names to ensure <mark>ai_input()</mark> works correctly.
- Debug Errors:
    - Handle potential errors like invalid ingredient names or missing data files.

7. Collaborate and Maintain
- Version Control:
    - Use Git for version control. Commit changes regularly.
- Testing and Feedback:
    - Test code regularly and share a feedback with me if you'll have any questions.
