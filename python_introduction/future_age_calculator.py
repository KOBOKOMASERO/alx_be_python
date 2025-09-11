# Python script that asks the user for their current age and then calculates how old they will be in a specific future year.

age = int(input("How old are you? "))
current_year = 2023
future_age = age + (2050 - current_year)
print(f"In 2050, you will be {future_age} years old.")
