Task = input("Enter your task: ").strip()
Priority = input("Priority (high/medium/low): ").strip().lower()
TimeBound = input("Is it time-bound? (yes or no): ").strip().lower()



# Validate and process priority
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

# Validate time-bound and print the appropriate message
if TimeBound == "yes":
    print(f"Reminder: '{Task}' is a {priority_text} priority Task that requires immediate attention today!")
elif TimeBound == "no":
    print(f"Note: '{Task}' is a {priority_text} priority Task. Consider completing it when you have free time.")
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    exit()
