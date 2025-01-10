from tabulate import tabulate # type: ignore
from wcwidth import wcswidth

emojis = {
    "smile": "😊",
    "laugh": "😂",
    "wink": "😉",
    "heart_eyes": "😍",
    "thinking": "🤔",
    "cry": "😢",
    "angry": "😠",
    "surprised": "😲",
    "cool": "😎",
    "sleepy": "😴",
    "cat": "🐱",
    "dog": "🐶",
    "mouse": "🐭",
    "rabbit": "🐰",
    "fox": "🦊",
    "panda": "🐼",
    "lion": "🦁",
    "tiger": "🐯",
    "bear": "🐻",
    "unicorn": "🦄",
    "apple": "🍎",
    "banana": "🍌",
    "cherry": "🍒",
    "watermelon": "🍉",
    "grapes": "🍇",
    "strawberry": "🍓",
    "pizza": "🍕",
    "burger": "🍔",
    "fries": "🍟",
    "ice_cream": "🍦",
    "sun": "☀️",
    "cloud": "☁️",
    "rain": "🌧️",
    "snowflake": "❄️",
    "lightning": "⚡",
    "flower": "🌸",
    "tree": "🌳",
    "cactus": "🌵",
    "mountain": "⛰️",
    "wave": "🌊",
    "car": "🚗",
    "bike": "🚴",
    "airplane": "✈️",
    "train": "🚆",
    "phone": "📱",
    "computer": "💻",
    "camera": "📷",
    "book": "📚",
    "gift": "🎁",
    "clock": "⏰",
    "heart": "❤️",
    "star": "⭐",
    "check_mark": "✔️",
    "cross_mark": "❌",
    "question_mark": "❓",
    "exclamation_mark": "❗",
    "peace": "☮️",
    "infinity": "♾️",
    "recycle": "♻️",
    "warning": "⚠️"
}


def adjust_width(text, width):
    padding = width - wcswidth(text)
    return text + " " * max(0, padding)


def display_emojis_tab():
    args_list = [_ for _ in emojis]

    table = []
    for i in range(0, len(emojis), 5):

        row = []
        for e in args_list[i:i+5]:
            text = f"{e} {emojis[e]}"
            row.append(adjust_width(text, 15))

        table.append(row)

    print(tabulate(table, tablefmt="fancy_grid", stralign="center"))
