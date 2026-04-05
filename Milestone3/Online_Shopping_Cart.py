""""
Milestone 3
Online Shopping Cart
Author: Shadab
"""

# Python code to calculate the total cost of all items and description of items in the Shopping Cart
# user provides Inputs at Runtime and also validations for inputs

from datetime import datetime

# ----------Item Class---------- #
class ItemToPurchase:

    # Constructor to Initialize Item Details
    def __init__(self, name = "none", price = 0.0, quantity = 0, description = "none"):
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity
        self.itemDescription = description

    # Method to Calculate and Display the Total Cost of the Item
    def print_item_cost(self):
        total_item_cost = self.itemPrice * self.itemQuantity
        print(f"\n{self.itemName} {self.itemQuantity} @ ${self.itemPrice} = ${total_item_cost}")

# Function to Validate the Purchased Item Name
def get_valid_name(prompt):
    while True:
        item_name = input(prompt).strip()

        # Validation of Empty Input
        if not item_name:
            print("Item Name cannot be Blank!! Please Enter Purchased Item Name.\n")

        elif not any(char.isalpha() for char in item_name):
            print("Warning!! Item Name must contain at least one alphabet!!\n")

        # Validation to prevent item names with only Numericals
        elif item_name.isnumeric():
            print("Warning!! Item Name cannot contains only Numerical Characters.\n")

        # Validation to check for Special Characters
        elif not item_name.replace(" ", "").isalnum():
            print("Warning!! Item Name cannot contains Special Characters.\n")

        else:
            return item_name

# Function to Validate the Purchased Item Quantity
def get_valid_item_quantity():
    while True:
        item_quantity = input("Enter Purchased Item Quantity: \n").strip()

        # Validation of Empty Input
        if item_quantity == "":
            print("Item Quantity cannot be Blank!! Please Enter Purchased Item Quantity.\n")
            continue

        try:
            # Converting Quantity to Integer
            quantity = int(item_quantity)

            # Validation to check if Quantity is Negative or Zero
            if quantity <= 0:
                print("Warning!! Purchased Item Quantity should be greater than 0.\n")

            # Validation to limit Quantity
            elif quantity > 10000:
                print("Warning!! Purchased Item Quantity is too high.\n")

            else:
                return quantity

        except ValueError:
            print("Warning!! Purchased Item Quantity must be an integer.\n")

# Function to Validate the Purchased Item Price
def get_valid_item_price():
    while True:
        item_price = input("Enter Purchased Item Price: \n").strip()

        # Validation of Empty Input
        if item_price == "":
            print("Item Price cannot be Blank!! Please Enter Purchased Item Price.\n")
            continue

        try:
            # Converting Price to Float
            price = float(item_price)

            # Validation to check if Price is Negative or Zero
            if price <= 0:
                print("Warning!! Purchased Item Price should be greater than 0.\n")

            else:
                return round(price, 2)

        except ValueError:
            print("Warning!! Purchased Item Price must be an integer.\n")

# Function to Get the Purchased Item Description
def get_valid_item_description():
    item_description = input("Enter Purchased Item Description: \n").strip()
    if len(item_description) > 100:
        print("Warning!! Purchased Item Description is too long.\n")
        return item_description[:100]
    return item_description if item_description else "None"


# ----------Shopping Cart Class---------- #
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Add Item to Cart
    def add_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.itemName.lower() == item.itemName.lower():
                print(f"Item {cart_item.itemName} already exists in cart.Use modify option to update\n")
                return

        self.cart_items.append(item)

    # Remove Item from Cart
    def remove_item(self, item_name):
        if not self.cart_items:
            print("Cart is empty. Nothing to remove.\n")
            return

        found = False

        for item in self.cart_items:
            if item.itemName.lower() == item_name.lower():
                found = True

                confirm = input(f"Do you want to Remove {item.itemName} from cart? (y/n).\n").lower()
                if confirm == "y":
                    self.cart_items.remove(item)
                    print("Item Removed Successfully, Removed Item " + item.itemName.lower())
                    return

        if not found:
            print(f"Warning!! Item {item_name} is not found in the cart. Nothing was Removed\n")

    # Modify Item Quantity
    def modify_item(self, item):
        if not self.cart_items:
            print("Cart is empty. Nothing to modify.\n")
            return

        found = False

        for cart_item in self.cart_items:
            if cart_item.itemName.lower() == item.itemName.lower():
                found = True

                if item.itemQuantity != 0:
                    cart_item.itemQuantity = item.itemQuantity

                if item.itemPrice != 0.0:
                    cart_item.itemPrice = item.itemPrice

                if item.itemDescription != "none":
                    cart_item.itemDescription = item.itemDescription

                print(f"Item {item.itemName} Modified Successfully")
                return

        if not found:
                print(f"Item {item.itemName} is not found in the cart. Nothing Modified\n")


    # Get Total Number of Items
    def get_num_items_in_cart(self):
        return sum(item.itemQuantity for item in self.cart_items)

    # Get Total Cost
    def get_cost_of_cart(self):
        return sum(item.itemPrice * item.itemQuantity for item in self.cart_items)

    # Print Total Cart Details
    def print_total(self):
        print("\n************ OUTPUT SHOPPING CART ************\n")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print(f"Number of Items in Cart: {self.get_num_items_in_cart()}")

        if not self.cart_items:
            print("\nShopping Cart is Empty.\n")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}\n")
            print('\n*************************************************\n')

    # Print Item Descriptions
    def print_descriptions(self):
        print("\n************ OUTPUT ITEM'S DESCRIPTIONS ************\n")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Shopping Cart Item Descriptions:\n")

        if not self.cart_items:
            print("\nShopping Cart is Empty.\n")
        else:
            for item in self.cart_items:
                print(f"{item.itemName}: {item.itemDescription}")
            print('\n***************************************************\n')

# ----------Shopping Cart Menu---------- #
def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add Item to Cart")
        print("r - Remove Item from Cart")
        print("c - Change Item Quantity")
        print("i - Output Item's descriptions")
        print("o - Output Shopping Cart")
        print("q - Quit")

        user_choice = input("\nChoose an option: \n").lower().strip()
        if user_choice == "a":
            print("\nADD ITEM TO CART")
            name = get_valid_name("Enter Purchased Item Name: \n")
            description = get_valid_item_description()
            price = get_valid_item_price()
            quantity = get_valid_item_quantity()
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)

        elif user_choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = get_valid_name("Enter item name in the cart to remove: \n")
            cart.remove_item(name)

        elif user_choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = get_valid_name("Enter item name in the cart to modify: \n")
            quantity = get_valid_item_quantity()
            item = ItemToPurchase(name = name, quantity = quantity)
            cart.modify_item(item)

        elif user_choice == "i":
            cart.print_descriptions()

        elif user_choice == "o":
            cart.print_total()

        elif user_choice == "q":
            print("\nExited Cart")
            break

        else:
            print("\nInvalid Choice!! Please Enter Valid Choice.\n")


# Main Function
def main():
    name = get_valid_name("Enter customer's name: \n")
    date = input("Enter today's date: \n").strip()
    if not date:
        date = datetime.now().strftime("%B %d, %Y")

    print(f"\nCustomer Name: {name}")
    print(f"Today's Date: {date}")

    cart = ShoppingCart(name, date)
    print_menu(cart)

if __name__ == "__main__":
    main()


