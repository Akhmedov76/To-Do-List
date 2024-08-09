import json
from contextlib import contextmanager


@contextmanager
def open_file(file_name, mode):
    file = open(file_name, mode)
    yield file
    file.close()


with open_file('users.json', 'w') as f:
    data = {
        'name': input("Enter your username: "),
        'age': int(input("Enter your age: ")),
        'birth_date': input("Enter your birth date: ")
    }
    json.dump(data, f, indent=4)
    print("User data saved successfully.")
