from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Returning so it can be reused if needed

def calculate_future_date(current_date, days_to_add):
    """
    Calculates and displays the future date after adding a specified number of days.

    Args:
        current_date (datetime): The starting date.
        days_to_add (int): Number of days to add.

    Returns:
        datetime: The calculated future date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    main()
