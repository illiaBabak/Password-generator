import random
import os
import shutil

VALID_RESPONSES = {"yes", "y", "no", "n"}

LETTERS = "abcdefghijklmnopqrstuvwxyz"
CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL_SYMBOLS = "@#_-"

FILE_NAME = "password.txt"
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DESTINATION_PATH = os.path.join(DOWNLOAD_PATH, FILE_NAME)

counter = 1

print(
    "Password Generator - a tool for creating strong passwords with minimal effort. Just select the parameters you need"
)


# A function that restarts the program
def restart():
    input("\nClick the button to start generating the password again")
    start()


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


# A function that checks the validity of inputs
def check_input(prompt):
    while True:
        user_input = input(prompt).lower()

        if user_input in VALID_RESPONSES:
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# A function that checks the validity of a number
def check_number(prompt):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid numeric value.")


# A function that save password
def save():
    global DESTINATION_PATH, counter

    if os.path.exists(DESTINATION_PATH):
        file_name_without_extension, file_extension = os.path.splitext(FILE_NAME)
        new_file_name = f"{file_name_without_extension}({counter}){file_extension}"
        DESTINATION_PATH = os.path.join(DOWNLOAD_PATH, new_file_name)
        counter += 1

    with open(FILE_NAME, "w") as file:
        file.write(password)

    shutil.move(FILE_NAME, DESTINATION_PATH)
    print(f"File saved in downloads: {DESTINATION_PATH}")
    restart()


# A function that starts the program
def start():
    global password

    inputs = [
        check_number("Enter the password length: "),
        *map(
            check_input,
            [
                "Use capital letters? (yes/no): ",
                "Use numbers? (yes/no): ",
                "Use special symbols like @, #, _, -? (yes/no): ",
            ],
        ),
    ]

    password = generate_password(*inputs)

    is_save = check_input(f"{password}\nSave password? (yes/no): ")

    if is_save.lower() in {"yes", "y"}:
        save()

    else:
        restart()


start()
