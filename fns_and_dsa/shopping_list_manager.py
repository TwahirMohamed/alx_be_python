# A python script that implements a simple interface for managing a shopping list.
# The task focuses on lists to store and manipulate data dynamically.

# Function for display menu
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
# Main program
def main():
    shopping_list = [] # Initializing with an empty list
    # Loop for continous display
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                # Add an item
                add_item = input("Enter the item to add: ")
                shopping_list.append(add_item)
                pass
            case 2:
                # Remove an item
                remove_item = input("Enter the item to remove: ")
                shopping_list.remove(remove_item) # used remove instead of pop since pop works for index 
                pass
            case 3:
                # View List
                print(shopping_list)
                pass
            case 4:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()