import os

from month_4.lesson_7.users.logs import log_decorator


class TxtManager:
    def __init__(self, filename):
        self.filename = filename

    def check_filename(self):
        return os.path.exists(self.filename)

    @log_decorator
    def read_file(self):
        if self.check_filename():
            if os.path.getsize(self.filename) != 0:
                with open(self.filename, "r") as file:
                    return file.read()
            return ""
        return ""

    @log_decorator
    def write_file(self, content):
        with open(self.filename, "w") as file:
            file.write(content)

    @log_decorator
    def append_to_file(self, content):
        with open(self.filename, "a") as file:
            content += "\n"
            file.write(content)


file_manager = TxtManager('posts/post.txt')
