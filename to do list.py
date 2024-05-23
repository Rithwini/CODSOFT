def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_item(todo_list, item):
    todo_list.append(item)
    print(f"Added '{item}' to your to-do list.")

def remove_item(todo_list, index):
    if index >= 1 and index <= len(todo_list):
        removed_item = todo_list.pop(index - 1)
        print(f"Removed '{removed_item}' from your to-do list.")
    else:
        print("Invalid index!")

def main():
    todo_list = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Display to-do list")
        print("2. Add item to to-do list")
        print("3. Remove item from to-do list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            item = input("Enter the item you want to add: ")
            add_item(todo_list, item)
        elif choice == '3':
            index = int(input("Enter the index of the item you want to remove: "))
            remove_item(todo_list, index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
