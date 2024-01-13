import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"
CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL_SYMBOLS = "@#_-"


# A function that generates a new password
def generate_password(length, has_capital_letters, has_numbers, has_special_symbols):
    res = LETTERS

    if has_capital_letters:
        res += CAPITAL_LETTERS

    if has_numbers:
        res += NUMBERS

    if has_special_symbols:
        res += SPECIAL_SYMBOLS

    password = "".join(random.choice(res) for _ in range(int(length)))
    return password
