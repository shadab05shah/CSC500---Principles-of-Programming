""""
Milestone 2
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
def get_valid_item_name(duplicate_items):
    while True:
        item_name = input("Enter Purchased Item Name: \n").strip()

        # Validation of Empty Input
        if item_name == "":
            print("Item Name cannot be Blank!! Please Enter Purchased Item Name.\n")

        # Validation to prevent item names with only Numericals
        elif item_name.isnumeric():
            print("Warning!! Item Name cannot contains only Numerical Characters.\n")

        # Validation to check for Special Characters
        elif not item_name.replace(" ", "").isalnum():
            print("Warning!! Item Name cannot contains Special Characters.\n")

        # Validation to check if the Item Name already Exists
        elif item_name.lower() in duplicate_items:
            print("Warning!! Item name already exists.\n")

        else:
            duplicate_items.add(item_name.lower())
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
        self.item_names = set()

    # Add Item to Cart
    def add_item(self, item):
        self.cart_items.append(item)
        self.item_names.add(item.itemName.lower())

    # Remove Item from Cart
    def remove_item(self, item_name):
        if not self.cart_items:
            print("Cart is empty. Nothing to remove.\n")
            return

        for item in self.cart_items:
            if item.itemName.lower() == item_name.lower():
                self.cart_items.remove(item)
                self.item_names.discard(item.itemName.lower())
                print("Item Removed Successfully, Removed Item " + item.itemName.lower())
                return

            print("Warning!! Item " + item.itemName + " is not found in the cart. Nothing was Removed\n")

    # Modify Item Quantity
    def modify_item(self, item_name):
        if not self.cart_items:
            print("Cart is empty. Nothing to modify.\n")
            return
        for item in self.cart_items:
            if item.itemName.lower() == item_name.lower():
                print("\nFor the Item " + item.itemName.lower() + "what needs to be modified:\n")
                print("1. Quantity\n")
                print("2. Price\n")
                print("3. Description\n")

                user_choice = input("Choose the option: \n").strip()

                if user_choice == "1":
                    item.itemQuantity = get_valid_item_quantity()

                elif user_choice == "2":
                    item.itemPrice = get_valid_item_price()

                elif user_choice == "3":
                    item.itemDescription = get_valid_item_description()

                else:
                    print("\nInvalid Choice!! Please Enter Valid Choice.\n")

                print("\nItem Updated Successfully.\n")
                return

        print("\nItem not found in the cart. Nothing modified\n")

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
            name = get_valid_item_name(cart.item_names)
            description = get_valid_item_description()
            price = get_valid_item_price()
            quantity = get_valid_item_quantity()
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)

        elif user_choice == "r":
            name = input("Enter item name in the cart to remove: \n").strip()
            cart.remove_item(name)

        elif user_choice == "c":
            name = input("Enter item name in the cart to modify: \n").strip()
            cart.modify_item(name)

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
    name = input("Enter customer's name: \n")
    date = datetime.now().strftime("%B %d, %Y")

    print(f"\nCustomer Name: {name}")
    print(f"Today's Date: {date}")

    cart = ShoppingCart(name, date)
    print_menu(cart)

if __name__ == "__main__":
    main()


