import json


class CustomOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with CustomOpen('users.json', 'w') as f:
    data = {
        "name": input("Enter your username: "),
        "age": int(input("Enter your age: ")),
        "birth_date": input("Enter your birth date (YYYY-MM-DD): ")
    }
    json.dump(data, f, indent=4)
    print("User data saved successfully.")
