# Prompt user for inputs
Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
TimeBound = input("Is it time-bound? (yes or no): ").lower()

# Process based on priority
match Priority:
    case "high":
        priority_text = "high"
    case "medium":
        priority_text = "medium"
    case "low":
        priority_text = "low"
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        exit()

# Process time-bound and print accordingly
if TimeBound == "yes":
    print(f"Reminder: '{Task}' is a {priority_text} priority task that requires immediate attention today!")
elif TimeBound == "no":
    print(f"Note: '{Task}' is a {priority_text} priority task. Consider completing it when you have free time.")
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()
