import sys

VALID_RESPONSES = {"yes", "y", "no", "n"}


# A function that checks the validity of inputs
def check_input(prompt):
    while True:
        user_input = input(prompt).lower()

        if user_input == "exit":
            sys.exit()

        if user_input in VALID_RESPONSES:
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
