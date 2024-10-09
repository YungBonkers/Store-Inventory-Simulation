import pickle

def save_inventory(current_items):
    with open('inventory_items.txt', 'wb') as file:
        pickle.dump(current_items, file)
        print("Inventory saved successfully!")

def load_inventory():
    try:
        with open('inventory_items.txt', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("No previous inventory found. Starting with an empty inventory.")
        return {}
    
