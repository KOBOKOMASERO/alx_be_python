try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2:.2f}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation.")