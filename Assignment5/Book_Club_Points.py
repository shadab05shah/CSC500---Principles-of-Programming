""""
Assignment 5 - - Part 2
Book Club Points Calculation
Author: Shadab
"""

# Python code to calculate the book club points based on number of books purchased in a month
# user provides Inputs at Runtime and also validations for inputs

while True:
    try:
        books_purchased = int(input("Enter the number of books purchased in this month: "))
        # Validation to check inputs for books purchased is not negative
        if books_purchased < 0:
            print("Warning!! Number of books purchased in this month cannot be negative.\n")
        else:
            break
    except ValueError:
        print("Error!! Please enter a valid integer value for number of books purchased.\n")

# Points based on Number of Books Purchased
if books_purchased == 0:
    book_points = 0
elif books_purchased == 2:
    book_points = 5
elif books_purchased == 4:
    book_points = 15
elif books_purchased == 6:
    book_points = 30
elif books_purchased >= 8:
    book_points = 60
else:
    book_points = "NA"
    print("\nWarning!! Points are awarded only for purchasing of 2, 4, 6, or 8+ books.")

print('\n**************** Book Club Points ****************\n')
print("Books Purchased (in Month)   :", books_purchased, "Books")
if book_points == "NA":
    print("Book Points Awarded          :", book_points, "(Invalid number of books for points calculation)")
else:
    print("Book Points Awarded          :", book_points, "Points")
print('\n**************************************************\n')


