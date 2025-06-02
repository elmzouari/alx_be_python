def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found in the shopping list.")
        elif choice == 3:
            for item in shopping_list:
                print(item)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

