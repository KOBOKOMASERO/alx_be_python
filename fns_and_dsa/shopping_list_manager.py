# shopping_list_manager.py

def display_menu():
    """Displays the main menu options."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty. Please try again.")

        elif choice == '2':
            # Remove an item from the shopping list
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' is not in your shopping list.")

        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '4':
            # Exit the program
            print("Goodbye! Thanks for using Shopping List Manager.")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
# A simple command-line shopping list manager application.