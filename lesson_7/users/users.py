from datetime import datetime
from month_4.lesson_7.txt_manager import file_manager
from month_4.lesson_7.users.logs import log_decorator


@log_decorator
def create_post():
    try:
        user_name = input("Enter your username: ").capitalize().strip()
        title = input("Enter the title of your post: ").capitalize().strip()
        message = input("Enter the content of your post: ").capitalize().strip()
        post_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        post = f"{user_name}, {title}, {message}, {post_date}"
        file_manager.append_to_file(post)
        print("Post created successfully!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


@log_decorator
def show_posts():
    try:
        posts = file_manager.read_file()
        for post in posts.split("\n"):
            if post:
                user_name, title, message, post_date = post.split(", ")
                print(f"User: {user_name}\nTitle: {title}\nMessage: {message}\nPost date: {post_date}\n")
            return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
