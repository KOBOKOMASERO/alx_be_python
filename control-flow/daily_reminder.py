# daily_reminder.py

# Prompt user for inputs (robustly)
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes or no): ").strip().lower()

# Validate and process priority
match priority:
    case "high":
        priority_text = "high"
    case "medium":
        priority_text = "medium"
    case "low":
        priority_text = "low"
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        exit()  # Stop execution for invalid input

# Validate time-bound and print the appropriate message
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: '{task}' is a {priority_text} priority task. Consider completing it when you have free time.")
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()
