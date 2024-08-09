import time

from admin.admin import add_movie, view_movies, edit_movie, delete_movie
from admin.users_manage import show_all_users, edit_user_profile, delete_user_account
from users.common import register, login, UserTypes, logout, reset_account_password
from users.logs import log_settings


def show_admin_menu():
    print("""
1. Manage all user data
2. Movie data management
3. ................
4. Exit
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        manage_user()
    elif choice == 2:
        add_movies()
    elif choice == 3:
        pass
    elif choice == 4:
        print("Exit successfully")
        return show_auth_menu()
    else:
        print("Invalid choice! Please try again.")
        show_admin_menu()


def manage_user():
    print("""
1. Show all user
2. Edit users data
3. Delete user
4. Exit
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_all_users()
        manage_user()
    elif choice == 2:
        edit_user_profile()
        manage_user()
    elif choice == 3:
        delete_user_account()
        manage_user()
    elif choice == 4:
        print("Exit successfully")
        return manage_user()
    else:
        print("Invalid choice! Please try again.")
        manage_user()


def add_movies():
    print("""
1. Add new movies 
2. Edit movies data
3. Delete movies
4. View all movies
5. Exit
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if add_movie():
            add_movies()
        else:
            add_movies()
    elif choice == 2:
        if edit_movie():
            add_movies()
        else:
            add_movies()
    elif choice == 3:
        if delete_movie():
            add_movies()
        else:
            add_movies()
    elif choice == 4:
        if view_movies():
            add_movies()
        else:
            add_movies()
    elif choice == 5:
        print("Exit successfully")
        return show_auth_menu()
    else:
        print("Invalid choice! Please try again.")
        add_movies()


def users_menu():
    print("""
1. Buy ticket
2. View purchased tickets
3. Connect the card
4. Exit   
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        connect_card()
    elif choice == 4:
        print("Exit successfully")
        return show_auth_menu()
    else:
        print("Invalid choice! Please try again.")
        users_menu()


def tickets_menu():
    print("""
1. List of movies|  naqd yoki kartada
2. Search movies by title|  naqd yoki kartada
3. View a list of movies by location|  naqd yoki kartada 
4. Exit
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Exit successfully")
        return show_auth_menu()
    else:
        print("Invalid choice! Please try again.")
        tickets_menu()


def connect_card():
    print("""
1. Attach card
2. Transfer money to the card account   
3. Check the status of the card account 
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        print("Invalid choice! Please try again.")
        connect_card()


def show_auth_menu():
    print("""
1. Register
2. Login
3. Password recovery
4. Exit""")

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
            users_menu()
        else:
            print("Invalid credentials!")
            show_auth_menu()
    elif user_input == "3":
        print("""
Invalid credentials!
If you forgot your code?. Do you want to reset it? Yes/No
""")
        time.sleep(1)
        choice = input("Enter your answer: ").lower()
        if choice == "yes":
            reset_account_password()
            show_auth_menu()
    elif user_input == "4":
        if logout():
            print("Goodbye!")
            exit()
        else:
            print("Logout canceled!😊")
            show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        show_auth_menu()


if __name__ == "__main__":
    log_settings()  # Enable logging for all functions in this module.
    show_auth_menu()
