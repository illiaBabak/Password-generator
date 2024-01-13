import os
import shutil
from check_input import check_input
from check_number import check_number
from generate_password import generate_password


FILE_NAME = "password.txt"
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DESTINATION_PATH = os.path.join(DOWNLOAD_PATH, FILE_NAME)

counter = 1


print(
    "Password Generator - a tool for creating strong passwords with minimal effort. Just select the parameters you neede a winner! Type 'exit'"
)


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


# A function that restarts the program
def restart():
    input("\nClick the button to start generating the password again")
    start()


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
