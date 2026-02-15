""""
Assignment 1 - Part 1
Arithmetic operations - Addition and Subtraction with input validations
Author: Shadab
"""

# Python code for Addition and Subtraction of numbers
# user provides Inputs at Runtime and also added inputted Value validations

from decimal import Decimal, InvalidOperation

# Validating First Number
while True:
    try:
        number1 = input("Enter Valid First Number (Positive or Negative): ").strip()

        # Checking if the provided input is empty and asking user to input valid values
        if number1 == "":
            print("Input value cannot be empty!! Please enter a valid number either positive or negative.\n")
            continue

        number1 = Decimal(number1)
        break

    except InvalidOperation:
        print("Invalid Input!! Please enter only numerical values either positive or negative.\n")


# Validating Second Number and Second Number input is asked only if the first number is valid
while True:
    try:
        number2 = input("Enter Valid Second Number (Positive or Negative): ").strip()

        # Checking if the provided input is empty and asking user to input valid values
        if number2 == "":
            print("Input value cannot be empty!! Please enter a valid number either positive or negative.\n")
            continue

        number2 = Decimal(number2)

        break

    except InvalidOperation:
        print("Invalid Input!! Please enter only numerical values either positive or negative.\n")

# Arithmetic Operations
addition = number1 + number2
subtraction = number1 - number2

print("\n***** Result Summary *****\n")
print("Result for Addition of Numbers:", addition)
print("Result for subtraction of Numbers:", subtraction)
