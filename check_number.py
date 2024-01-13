import sys


# A function that checks the validity of a number
def check_number(prompt):
    while True:
        user_input = input(prompt)

        if user_input == "exit":
            sys.exit()

        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid numeric value.")
