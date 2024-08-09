import hashlib
import random
import smtplib
import threading
from datetime import datetime
from enum import Enum
from file_manager import users_manager
from users.logs import log_decorator

Admin_login = "admin"
Admin_password = "admin"


class UserTypes(str, Enum):
    ADMIN = "Admin"
    USER = "user"


class User:
    def __init__(self, full_name, username, gmail, password, age, gender, date):
        self.full_name = full_name
        self.username = username
        self.gmail = gmail
        self.password = password
        self.age = age
        self.gender = gender
        self.date = date
        self.is_login = False

    def check_password(self, confirm_password):
        return confirm_password == self.password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_username(username: str):
        # Username verification function
        all_users = users_manager.read()
        for user in all_users:
            if user['username'] == username:
                return username


def check_gmail_account(gmail):
    data = users_manager.read()
    for user in data:
        if user['gmail'] == gmail:
            return True
    return False


def check_gmail(gmail):
    # A function to verify that an address is actually a Gmail address
    if '@' in gmail:
        return True
    return False


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'ahmedovj7686@gmail.com'
smtp_password = 'xnuj mftg hmqz xtow'


def send_mail(to_user, subject, message):
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


@log_decorator
def register() -> bool:
    try:
        full_name = input("Enter your full name: ").title().strip()
        username = input("Enter username: ").capitalize().strip()

        if User.check_username(username):
            print("Username already exists")
            return register()

        gmail = input("Enter email address: ").strip().lower()
        if check_gmail_account(gmail):
            print("Email already exists")
            return register()
        if not check_gmail(gmail):
            print("Invalid email address")
            return register()

        if not gmail.endswith('gmail.com'):
            gmail += 'gmail.com'

        user_subject = "Verification code:"
        user_code = random.randint(1000, 9999)
        print(user_code)
        threading.Thread(target=send_mail, args=(gmail, user_subject, user_code)).start()
        print("Email sent successfully, please check your gmail address")

        user_entered_code = int(input("Enter your verification code: "))
        if user_entered_code != user_code:
            print("Invalid verification code")
            return register()

        password = input("Enter your password: ").strip()
        confirm_password = input("Confirm your password: ").strip()
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (Male/Female): ").capitalize().strip()
        date = datetime.now().strftime("%Y.%m.%d %H.%M")
        users = User(full_name, username, gmail, password, age, gender, date)

        if not users.check_password(confirm_password):
            print("Passwords do not match")
            return register()

        users.password = User.hash_password(password)
        users_manager.add_data(data=users.__dict__)
        print("🎉Successfully registered🎉")
        return True

    except Exception as e:
        print(f"Something went wrong {e}")
        return False


def find_user(gmail, password):
    all_users = users_manager.read()
    for user in all_users:
        if user['gmail'] == gmail and user['password'] == password:
            return True
    return False


@log_decorator
def login() -> dict[str, str] | bool:
    gmail = input("Enter your gmail address: ").lower().strip()
    password = input("Enter your password: ").strip()
    hashed_password = User.hash_password(password)
    if gmail == Admin_login and password == Admin_password:
        print("Welcome to Admin👮‍♂️")
        return {'user_type': UserTypes.ADMIN.value}
    elif find_user(gmail, hashed_password):
        data = users_manager.read()
        for user in data:
            if user['gmail'] == gmail and user['password'] == hashed_password:
                user['is_login'] = True
                users_manager.write(data)
                print(f'Welcome to the user menu: {user["username"]}🎉')
        return {'user_type': UserTypes.USER.value}
    else:
        return False


def reset_account_password() -> bool:
    try:
        users = users_manager.read()
        gmail = input("Enter email address: ").strip().lower()
        if not check_gmail(gmail):
            print("Invalid email address")
            return register()
        if not gmail.endswith('gmail.com'):
            gmail += 'gmail.com'
        for user in users:
            if user['gmail'] == gmail:
                user_subject = "Reset password code:"
                user_code = random.randint(1000, 9999)
                print(user_code)
                threading.Thread(target=send_mail, args=(gmail, user_subject, user_code)).start()
                print("Email sent successfully, please check your gmail address")

                user_entered_code = int(input("Enter your verification code: "))
                if user_entered_code != user_code:
                    print("Invalid verification code")
                    return False
                new_password = input("Enter your new password: ").strip()
                confirm_new_password = input("Confirm your new password: ").strip()
                if not new_password == confirm_new_password:
                    print("Passwords do not match")
                    return False
                user['password'] = User.hash_password(new_password)
                users_manager.write(users)
                print("Your password has been reset successfully")
                return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def logout():
    try:
        txt = """
Are you sure you want to exit😱? Yes or No
        """
        print(txt)
        choice = (input("Enter your answer: ").lower())
        if choice == "yes":
            read = users_manager.read()
            for user in read:
                user["is_login"] = False
                users_manager.write(read)
            return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
