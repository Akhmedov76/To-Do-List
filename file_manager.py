import os
import json


class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_exists_and_not_empty(self):
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read(self):
        if self.file_exists_and_not_empty():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def write(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def add_data(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        self.write(all_data)
        return "Data added successfully"


data_manager = JsonManager("data/datas.json")
