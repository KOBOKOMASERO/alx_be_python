try:
    size = int(input("Enter the size of the pattern: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    size = 0

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
