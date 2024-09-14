# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    return sorted_products


def display_products(products_list):
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product}: ${price}")


def display_categories():
    print("Available Categories:")
    for i, category in enumerate(products, start=1):
        print(f"{i}. {category}")


def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))


def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print("Your cart contains:")
    for product, quantity in cart:
        print(f"{product}: {quantity}")


def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Items purchased:")
    for product, quantity in cart:
        print(f"{product}: {quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")


def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email


def main():
    # Ask for user name and validate
    name = input("Enter your name (First and Last name): ")
    while not validate_name(name):
        print("Invalid name. Please enter both first and last names, containing only letters.")
        name = input("Enter your name (First and Last name): ")
    
    # Ask for user email and validate
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please include an '@' in the email address.")
        email = input("Enter your email: ")
    
    # Display categories and let user choose one
    cart = []
    total_cost = 0
    while True:
        display_categories()
        try:
            category_choice = int(input("Choose a category by entering the corresponding number: "))
            if category_choice not in range(1, len(products) + 1):
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue
            
        # Get the category and products list
        category_name = list(products.keys())[category_choice - 1]
        products_list = products[category_name]

        while True:
            display_products(products_list)
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = input("Choose an option: ")

            if option == "1":
                try:
                    product_choice = int(input("Enter the product number to buy: "))
                    if product_choice not in range(1, len(products_list) + 1):
                        raise ValueError
                except ValueError:
                    print("Invalid product choice.")
                    continue
                
                product_name, product_price = products_list[product_choice - 1]
                quantity = int(input(f"Enter the quantity of {product_name}: "))
                add_to_cart(cart, product_name, quantity)
                total_cost += product_price * quantity

            elif option == "2":
                sort_order = int(input("Enter 1 to sort by ascending price or 2 for descending: "))
                sorted_products = display_sorted_products(products_list, sort_order)
                display_products(sorted_products)

            elif option == "3":
                break

            elif option == "4":
                if cart:
                    display_cart(cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time.")
                return  # Exit the program after finishing shopping

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
