import ijson
from month_4.alone_project.alone_project.file_manager import users_manager


def show_all_users():
    # Read users data from file
    with open('./data/users.json', 'r') as file:
        users_data = ijson.items(file, 'item')
        for users in users_data:
            print(
                f"username: {users['username']}\ngmail: {users['gmail']}\nage: {users['age']}\ngender: "
                f"{users['gender']}\n")


def edit_user_profile():
    try:
        user_data = users_manager.read()
        for user in user_data:
            if user['is_login']:
                new_full_name = input("Enter full name: ")
                new_age = int(input("Enter age: "))
                new_gender = input("Enter gender: ")
                user['full_name'] = new_full_name
                user['age'] = new_age
                user['gender'] = new_gender
                users_manager.write(user_data)
                print("Profile updated successfully.")
                return True
    except FileNotFoundError:
        print("User data file not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def delete_user_account():
    try:
        user_data = users_manager.read()
        for user in user_data:
            if user['is_login']:
                del user_data[user_data.index(user)]
                users_manager.write(user_data)
                print("User account deleted successfully.")
                return True
    except FileNotFoundError:
        print("User data file not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
