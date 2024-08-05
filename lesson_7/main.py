from month_4.lesson_7.users.admin import show_all_users, show_all_posts,search_posts
from month_4.lesson_7.users.common import logout, register, login, UserTypes
from month_4.lesson_7.users.logs import log_settings
from month_4.lesson_7.users.users import create_post, show_posts


def show_admin_menu():
    text = """
1. Show all users
2. Show all posts
3. Search with keywords
4. Exit
    """
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if show_all_users():
            show_admin_menu()
        else:
            print("Failed to show users. Please try again.")
            show_admin_menu()  # go back to admin menu again if failed to show users.

    elif user_input == "2":
        if show_all_posts():
            show_admin_menu()
        else:
            print("Failed to show posts. Please try again.")
            show_admin_menu()
    elif user_input == "3":
        if search_posts():
            show_admin_menu()
        else:
            print("Failed to search posts. Please try again.")
            show_admin_menu()
    elif user_input == "4":
        print("Exit successfully!")
        show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        show_admin_menu()


def user_menu():
    print("""
1. Create a post
2. Get my all posts
3. Logout
    """)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        if create_post():
            user_menu()
        else:
            print("Failed to create a post. Please try again.")
            user_menu()
    elif user_input == "2":
        if show_posts():
            user_menu()
        else:
            print("Failed to get your posts. Please try again.")
            user_menu()
    elif user_input == "3":
        print("Goodbye!���")
        show_auth_menu()


def show_auth_menu():
    print("""
1. Register
2. Login
3. Exit""")
    # print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if register():
            show_auth_menu()
    elif user_input == "2":
        user = login()
        if not user:
            print("Invalid username and password. Please try again.")
            show_auth_menu()
        elif user['user_type'] == UserTypes.ADMIN.value:
            show_admin_menu()
        elif user['user_type'] == UserTypes.USER.value:
            user_menu()
        else:
            print("Invalid credentials!")
            show_auth_menu()
    elif user_input == "3":
        if logout():
            print("Goodbye!🥹")
        else:
            print("Logout canceled!😊")
            show_auth_menu()

    else:
        print("Invalid input. Please try again.")
        show_auth_menu()


if __name__ == "__main__":
    log_settings()  # Enable logging for all functions in this module.
    show_auth_menu()
