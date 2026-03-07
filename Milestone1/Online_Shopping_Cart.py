""""
Milestone 1
Online Shopping Cart
Author: Shadab
"""

# Python code to calculate the total cost of all items in the Shopping Cart
# user provides Inputs at Runtime and also validations for inputs

class ItemToPurchase:

    # Constructor to Initialize Item Details
    def __init__(self, name = "none", price = 0.0, quantity = 0):
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity

    # Method to Calculate and Display the Total Cost of the Item
    def print_item_cost(self):
        total_item_cost = self.itemPrice * self.itemQuantity
        print(f"\n{self.itemName} {self.itemQuantity} @ ${self.itemPrice} = ${total_item_cost}")

# Function to Validate the Purchased Item Name
def get_valid_item_name(existing_items):
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
        elif item_name.lower() in existing_items:
            print("Warning!! Item name already exists.\n")

        else:
            existing_items.add(item_name.lower())
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

# Function to Validate the Number of Items Purchased
def get_number_of_items():
    while True:
        # Prompt User for Number of Items Purchased
        number_of_items = input("Enter Number of Items Purchased:\n").strip()

        # Validation of Empty Input
        if number_of_items == "":
            print("Number of Items cannot be Blank!! Please Enter Number of Items Purchased.\n")
            continue

        try:
            number_of_items = int(number_of_items)

            # Validation to check if Number of items is Negative or Zero
            if number_of_items <= 0:
                print("Warning!! Purchased Number of Items should be greater than 0.\n")

            # Validation to limit Number of Items
            elif number_of_items > 100:
                print("Warning!! Purchased Number of Items are too many.\n")

            else:
                return number_of_items

        except ValueError:
            print("Warning!! Purchased Number of Items must be an integer.\n")

# Function to Get Item Details
def get_item_details(item_number, existing_items):

    print(f"\nItem {item_number} \n")

    name = get_valid_item_name(existing_items)
    quantity = get_valid_item_quantity()
    price = get_valid_item_price()

    return ItemToPurchase(name, price, quantity)

# Main Function
def main():
    items = []
    existing_items = set()

    number_of_items = get_number_of_items()

    for i in range(1, number_of_items + 1):
        item = get_item_details(i, existing_items)
        items.append(item)

    print("\n************ TOTAL COST ************\n")

    total_cost = 0

    for item in items:
        item.print_item_cost()
        total_cost += item.itemPrice * item.itemQuantity

    print(f"\nTotal: ${round(total_cost, 2)}\n")
    print('\n*************************************\n')


if __name__ == "__main__":
    main()


