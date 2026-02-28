""""
Assignment 3 - Part 1
Restaurant Bill Calculator considering Tip & Tax along with Meal Charge
Author: Shadab
"""

# Python code for Restaurant Bill Calculator
# user provides Inputs at Runtime and also validations

from decimal import Decimal, InvalidOperation

# Define Constants
TIP_PERCENT = Decimal('0.18')
TAX_PERCENT = Decimal('0.07')
MIN_AMOUNT = Decimal('0.50')
MAX_AMOUNT = Decimal('10000.00')

# Function to Input and Validate food charge
def get_food_charge():
    while True:
        user_input = input('Enter the food charge: ').strip()

        #Validations for the input provided
        #Empty Input
        if user_input == '':
            print('Input value cannot be empty!! Please enter a valid food charge.\n')
            continue

        try:
            food_charge = Decimal(user_input)

            # Positive Input Value
            if food_charge <= 0:
                print(f'Invalid Input!! Please enter a valid amount greater than ${MIN_AMOUNT}.\n')
                continue

            # Minimum Input Value
            if food_charge < MIN_AMOUNT:
                print(f'Warning!! Amount entered must be at least ${MIN_AMOUNT}.\n')
                continue

            # Maximum Input Value
            if food_charge > MAX_AMOUNT:
                print(f'Warning!! Amount entered must be at most ${MAX_AMOUNT}.\n')
                continue

            # Number of Decimal places in the input value
            if food_charge.as_tuple().exponent < -2:
                print('Warning!! Please enter the Amount upto 2 decimal places.\n')
                continue

            return food_charge

        except InvalidOperation:
            print('Invalid Input!! Please enter only valid numerical amount.\n')

# Function to calculate the bill
def calculate_bill(food_charge):
    tip_amount = (food_charge * TIP_PERCENT).quantize(Decimal('0.01'))
    tax_amount = (food_charge * TAX_PERCENT).quantize(Decimal('0.01'))
    total_bill = (food_charge + tip_amount + tax_amount).quantize(Decimal('0.01'))
    return tip_amount, tax_amount, total_bill

# Function to generate the bill
def generate_bill(food_charge, tip_amount, tax_amount, total_bill):
    print('\n****** Bill Summary ******\n')
    print(f'Food Charge     : {food_charge:.2f}')
    print(f'Tip Amount (18%): {tip_amount:.2f}')
    print(f'Tax Amount (7%) : {tax_amount:.2f}')
    print(f'Total Bill      : {total_bill:.2f}')
    print('\n**************************\n')

def main():
    food_charge = get_food_charge()
    tip_amount, tax_amount, total_bill = calculate_bill(food_charge)
    generate_bill(food_charge, tip_amount, tax_amount, total_bill)

if __name__ == '__main__':
    main()