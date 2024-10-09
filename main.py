import menu
from menu import valid_items
from saved_inventory import save_inventory
from saved_inventory import load_inventory

valid_menu_items = valid_items() # This list validates the user choice to check if the choice is on the menu.

current_items = load_inventory()

def add_item():
    while True:
        added_item = input("Please select an item to add to your inventory: ").lower().strip()
        added_qty = input("How many of these items would you like to add?: ").strip()

        try:
            added_qty = int(added_qty)
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if added_item in valid_menu_items:
            if added_item in current_items:
                current_items[added_item] += added_qty  # Increment quantity
            else:
                current_items[added_item] = added_qty  # Add new item to inventory
            print(f"({added_qty}) {added_item} added to your inventory.")
            save_inventory(current_items)
        else:
            print("Invalid selection. Please select again.")

        another = input("Would you like to add another item? (yes/no): ").lower().strip()
        if another != 'yes':
            break

def remove_item():
    while True:
        removed_item = input("Please select an item to remove from your inventory: ").lower().strip()
        removed_qty = input("How many of these items would you like to remove?: ").strip()

        try:
            removed_qty = int(removed_qty)
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue  

        if removed_item in valid_menu_items:
            if removed_item in current_items:
                if current_items[removed_item] >= removed_qty:  # Ensure enough items to remove
                    current_items[removed_item] -= removed_qty  # Decrease quantity
                    if current_items[removed_item] == 0:
                        current_items.pop(removed_item)  # Remove item if quantity is 0
                    print(f"({removed_qty}) {removed_item} removed from your inventory.")
                    save_inventory(current_items)
                else:
                    print(f"You only have {current_items[removed_item]} of {removed_item}. Cannot remove {removed_qty}.")
            else:
                print(f"{removed_item} is not in your inventory.")
        else:
            print("Invalid selection. Please select again.")

        another = input("Would you like to remove another item? (yes/no): ").lower().strip()
        if another != 'yes':
            break

def update_quantity():
    while True:
        item = input("Please enter the item you would like to update: ")
        qty_num = input("Please select a quantity: ")
        add_or_subtract = input("Would you like to add or remove an item?: ").lower().strip()

        try:
            qty_num = int(qty_num)
            if qty_num <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue 

        if item in valid_menu_items:
            if item in current_items:
                if add_or_subtract == "add":
                    current_items[item] += qty_num  # Increment quantity
                elif add_or_subtract == "remove":
                    if current_items[item] >= qty_num:
                        current_items[item] -= qty_num
                        if current_items[item] == 0:
                            current_items.pop(item)
                        print(f"{qty_num} {item} removed from your inventory")
                    else:
                        print(f"You only have {current_items[item]} of {item}. Cannot remove {qty_num}")
                save_inventory(current_items)
            else:
                print("{item} is not in your inventory. Please add it first.")
        else:
            print("Invalid selection. Please try again.")

        another = input("Would you like to update another item? (Yes/No)").lower().strip()
        if another != "yes":
            break

def display_inventory():
    if current_items:
        print("\nCurrent Inventory:")
        for item, qty in current_items.items():
            print(f"{item.title()}: {qty}")
    else:
        print("\n Your inventory is empty.")

def search_inventory():
    search_method = input("Would you like to search by (1) Name or (2) Quantity Range? (Enter 1 or 2): ")

    if search_method == '1':
        # Search by name
        search_term = input("Enter the item name to search for: ").lower().strip()
        found_items = {item: qty for item, qty in current_items.items() if search_term in item}
        
        if found_items:
            print("\nSearch Results by Name:")
            for item, qty in found_items.items():
                print(f"{item.title()}: {qty}")
        else:
            print("No items found matching your search by name.")

    elif search_method == '2':
        # Search by quantity range
        try:
            min_qty = int(input("Enter the minimum quantity: "))
            max_qty = int(input("Enter the maximum quantity: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers for quantity.")
            return

        found_items = {item: qty for item, qty in current_items.items() if min_qty <= qty <= max_qty}
        
        if found_items:
            print("\nSearch Results by Quantity Range:")
            for item, qty in found_items.items():
                print(f"{item.title()}: {qty}")
        else:
            print("No items found in the specified quantity range.")

    else:
        print("Invalid selection. Please enter 1 or 2.")


                    
            

def main():
    print("Welcome to your Store Inventory!")
    print("\nHere is our menu: ")
    menu.display_menu()
    
    while True: 

        print("Choose an option below to update or display items in your inventory:")
        
        user_input = input("(Add Item / Remove Item / Update Quantity / Display Inventory / Search Inventory / Exit) : ").lower().strip()
        
        if user_input == "add item":
            add_item()
        elif user_input == "remove item":
            remove_item()
        elif user_input == "update quantity":
            update_quantity()
        elif user_input == "display inventory":
            display_inventory()
        elif user_input == "exit":
            save_inventory(current_items)
            print("Thank you for using the inventory system. Goodbye!")
            break  
        else:
            print("Invalid selection. Please choose a valid option.")

main()

