""""
Assignment 5 - - Part 1
Average Rainfall Calculation
Author: Shadab
"""

# Python code to calculate the average rainfall over the period of years using nested loops
# user provides Inputs at Runtime and also validations for inputs

total_inches_of_rainfall = 0.0
total_months_count = 0

# Validation for Number of Years Input
while True:
    try:
        total_years = int(input("Enter the total number of years over which average rainfall to be calculated: "))

        if total_years <= 0:
            print("Warning!! Please enter a valid positive integer for total number of years.\n")
        else:
            break
    except ValueError:
        print("Error!! Please enter a valid positive integer for total number of years.\n")

# outer loop will iterate once for each year
for year in range(1, total_years + 1):
    print(f"\nYear {year}")

    # Inner loop will iterate twelve times, once for each month
    for month in range(1, 13):

        #Validate Inches of Rainfall Input
        while True:
            try:
                rainfall_in_inches = float(input(f"Enter the rainfall in inches for month {month}: "))

                if rainfall_in_inches < 0:
                    print("Warning!! Please enter a valid positive value for rainfall in inches.\n")
                else:
                    break
            except ValueError:
                print("Error!! Please enter a valid positive value for rainfall in inches.\n")

        total_inches_of_rainfall += rainfall_in_inches
        total_months_count += 1

average_rainfall_in_inches = total_inches_of_rainfall / total_months_count

print('\n******************** Results ********************\n')
print("Total Months                           :", total_months_count)
print("Total Rainfall (in Inches)             :", format(total_inches_of_rainfall, ".2f"))
print("Average Rainfall per Month (in Inches) :", format(average_rainfall_in_inches, ".2f"))
print('\n**************************************************\n')