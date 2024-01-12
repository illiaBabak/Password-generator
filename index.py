import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"
CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL_SYMBOLS = "@#_-"

print(
    "Password Generator - a tool for creating strong passwords with minimal effort. Just select the parameters you need"
)


# A function that generates a new password
def generate_password(length, has_capital_letters, has_numbers, has_special_symbols):
    res_string_string = LETTERS

    if has_capital_letters:
        res_string_string += CAPITAL_LETTERS

    if has_numbers:
        res_string_string += NUMBERS

    if has_special_symbols:
        res_string_string += SPECIAL_SYMBOLS

    password = "".join(random.choice(res_string_string) for _ in range(length))
    return password


# A function that checks the validity of entered data
def check(length_text, capital_letters_text, numbers_text, special_symbols_text):
    length = 0

    try:
        length = int(length_text)
    except ValueError:
        print("Please enter a valid value.")
        start()

    capital_letters = capital_letters_text.lower() in {"yes", "y"}
    numbers = numbers_text.lower() in {"yes", "y"}
    special_symbols = special_symbols_text.lower() in {"yes", "y"}

    return length, capital_letters, numbers, special_symbols


def start():
    length_text = input("Enter the password length: ")
    capital_letters_text = input("Use capital letters? (yes/no)")
    numbers_text = input("Use numbers? (yes/no)")
    special_symbols_text = input("Use special symbols like @, #, _, - ? (yes/no)")

    inputs = check(
        length_text, capital_letters_text, numbers_text, special_symbols_text
    )

    if inputs:
        length, capital_letters, numbers, special_symbols = inputs
        print(generate_password(length, capital_letters, numbers, special_symbols))


start()
