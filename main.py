import random
import math
from constants import chars_numbers, chars_lower, chars_specials, chars_upper
from create_strong_password import create_strong_password

def gen_random_password():
    length = input(
        "Please, type a length for your password (press enter to use 8): ")
    if length:
        length = int(length)
    else:
        length = 8

    number_of_characters = math.floor(length / 4)

    password = []

    # numbers
    password.extend(random.choices(chars_numbers, k=number_of_characters))

    # lowercase chars
    password.extend(random.choices(chars_lower, k=number_of_characters))

    # uppercase chars
    password.extend(random.choices(chars_upper, k=number_of_characters))

    # special chars
    password.extend(random.choices(chars_specials, k=number_of_characters))

    random.shuffle(password)

    password = ''.join(password)

    print("Your password is:", password)

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

def menu():
    print("-- Password generator --")
    print("What do you want to do")
    print("1 - Generate a fully random password")
    print("2 - Create a strong password easy to remember")

    choice = input("Your choice: ")

    if choice == "1":
        gen_random_password()
    elif choice == "2":
        create_strong_password()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    menu()
