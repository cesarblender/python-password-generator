import random
import math
from constants import chars_numbers, chars_lower, chars_specials, chars_upper

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