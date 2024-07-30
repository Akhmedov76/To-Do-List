from month_4.lesson_5.file_manager import data_manager


def check_product_id(product_id):
    products = data_manager.read()
    if product_id in products.keys():
        return True
    return False


def add_product():
    product_id = input("Enter product ID: ").isalnum()
    if check_product_id(product_id):
        print("Product ID already exists")
        return add_product()
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ").isalnum()
    product_quantity = input("Enter product quantity: ")
    product_colour = input("Enter product colour: ")

    data = {
        "product_id": product_id,
        "product_name": product_name,
        "product_price": product_price,
        "product_quantity": product_quantity,
        "product_colour": product_colour
    }
    if data_manager.read(data.__dict__):
        print("Product is added successfully")
        return show_menu()
    print("Product does not added")


def show_menu():
    txt = """
1. Add product
2. Exit
    """
    print(txt)
    user_input = int(input("Choose from menu: "))
    if user_input == 1:
        pass
    elif user_input == 2:
        print("Goodbye")
        return


if __name__ == "__main__":
    show_menu()
