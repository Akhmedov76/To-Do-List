from month_4.lesson_7.txt_manager import file_manager
from month_4.lesson_7.users.logs import log_decorator
from month_4.lesson_7.file_manager import data_manager


@log_decorator
def show_all_users():
    try:
        data = data_manager.read()
        if data:
            for user in data:
                print(f"Username: {user['username']}\n"
                      f"Email: {user['email']}\n"
                      f"fullname: {user['full_name']}\n"
                      f"creat date: {user['date']}\n")
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


@log_decorator
def show_all_posts():
    try:
        posts = file_manager.read_file()
        for post in posts.split("\n"):
            if post:
                user_name, title, message, post_date = post.split(", ")
                print(f"User: {user_name}")
                print(f"Title: {title}")
                print(f"Message: {message}")
                print(f"Post date: {post_date}")
                print("-" * 20)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


@log_decorator
def search_posts():
    try:
        keyword = input("Enter keyword to search: ").capitalize()
        posts = file_manager.read_file()
        found_posts = []
        for post in posts.split("\n"):
            if post:
                user_name, title, message, post_date = post.split(", ")
                if keyword in user_name or keyword in title or keyword in message:
                    found_posts.append(post)
        print(found_posts)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
