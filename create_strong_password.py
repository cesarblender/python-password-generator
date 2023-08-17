import random
from constants import chars_numbers, chars_specials


def create_strong_password():
    text = input(
        "Enter a text easy to remember to make it stronger (default: \"password\"): ")

    if not text:
        text = "password"

    new_text = ""

    new_text += random.choice(chars_numbers)
    new_text += random.choice(chars_specials)

    for char in text:
        new_text += random.choice([char.lower(), char.upper()])

    new_text += random.choice(chars_specials)
    new_text += random.choice(chars_numbers)

    print(new_text)
