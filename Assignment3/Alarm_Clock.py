""""
Assignment 3 - Part 2
24-Hour Alarm Clock Program
Author: Shadab
"""

# Python code for 24-Hour Alarm Clock Program - With AM/PM Display
# user provides Inputs at Runtime and also validations

#Function to input and Validate Current time
def get_current_time():
    while True:
        user_input = input('Enter current time (0-23): ').strip()

        # Validations for the input provided
        # Empty Input
        if user_input == '':
            print('Input value cannot be empty!! Please enter a valid time.\n')
            continue

        # Enter value must be integer
        try:
            current_time = int(user_input)
        except ValueError:
            print('Warning!! Please enter a valid Integer Value.\n')
            continue

        # Enter value must be within the range of 0 to 23
        if current_time < 0 or current_time > 23:
            print('Warning!! Current time must be between 0 and 23.\n')
            continue

        return current_time

#Function to input and Validate wait hours
def get_wait_time():
    while True:
        user_input = input('Enter number of hours to wait: ').strip()

        # Validations for the input provided
        # Empty Input
        if user_input == '':
            print('Input value cannot be empty!! Please enter a valid number.\n')
            continue

        # Enter value must be integer
        try:
            wait_hours = int(user_input)
        except ValueError:
            print('Warning!! Please enter a valid Integer Value.\n')
            continue

        # Validation for negative values
        if wait_hours < 0:
            print('Invalid Input!! Hours to wait cannot be negative.\n')
            continue

        return wait_hours

# Function to calculate alarm time
def calculate_alarm_time(current_time, wait_hours):
    return (current_time + wait_hours) % 24

# Function to conver 24-hour to 12-hour format
def convert_to_12_hour_format(hour):
    if hour == 0:
        return 12, 'AM'
    elif 1 <= hour < 12:
        return hour, 'AM'
    elif hour == 12:
        return 12, 'PM'
    else:
        return hour - 12, 'PM'

def main():
    current_time = get_current_time()
    wait_hours = get_wait_time()

    alarm_time = calculate_alarm_time(current_time, wait_hours)

    current_12_format, current_period = convert_to_12_hour_format(current_time)
    alarm_12_format, alarm_period = convert_to_12_hour_format(alarm_time)

    hour_label = 'hr' if wait_hours == 1 else 'hrs'

    print("\n************ Alarm Summary ************\n")
    print(f'Current Time (24-hour)   : {current_time:02d}:00\n')
    print(f'Current Time (12-hour)   : {current_12_format:02d}:00 {current_period}\n')
    print(f'Wait Time (in hours)     : {wait_hours} {hour_label}\n')
    print(f'Alarm Time (24-hour)     : {alarm_time:02d}:00\n')
    print(f'Alarm Time (12-hour)     : {alarm_12_format:02d}:00 {alarm_period}\n')
    print("\n**************************************\n")

if __name__ == '__main__':
    main()