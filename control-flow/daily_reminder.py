
# Prompt user for inputs
Task = input("Enter your task: ")
TimeBound = input("Is it time-bound? (yes or no): ").lower()
Priority = input("Enter priority (high, medium, low): ").lower()

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
        exit()  # Stop execution for invalid input

# Process time-bound
if TimeBound == "yes":
    time_text = "that requires immediate attention today!"
elif TimeBound == "no":
    time_text = "Consider completing it when you have free time."
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()


print(f"Reminder: '{Task}' is a {priority_text} priority task {time_text}")
