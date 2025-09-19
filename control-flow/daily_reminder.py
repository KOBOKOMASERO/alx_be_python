
# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Enter priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

# Process based on priority
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

# Process time-bound
if time_bound == "yes":
    time_text = "that requires immediate attention today!"
elif time_bound == "no":
    time_text = "Consider completing it when you have free time."
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()


print(f"Reminder: '{task}' is a {priority_text} priority task {time_text}")
