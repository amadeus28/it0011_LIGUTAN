class Item:
    def __init__(self, item_id, name, description, price):
        if item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.id = item_id
        self.name = name.strip()
        self.description = description.strip()
        self.price = price

class ItemManagement(Item):
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Item ID already exists!")
            return
        try:
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print("Error:", e)
    
    def display_items(self):
        if not self.items:
            print("No items to display.")
        else:
            for item in self.items.values():
                print("ID:", item.id, "Name:", item.name, "Description:", item.description, "Price:", item.price,"Php")
    
    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Item ID not found!")
            return
        
        item = self.items[item_id]
        if name:
            item.name = name.strip()
        if description:
            item.description = description.strip()
        if price is not None and price >= 0:
            item.price = price
        print("Item updated successfully!")
    
    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item ID not found!")

def main():
    itemManager = ItemManagement()
    while True:
        print("\nItem Management Application (CREATE, READ, UPDATE, DELETE)")
        print("1. Add Item\n2. Display Items\n3. Update Item\n4. Delete Item\n5. Exit")
        choice = input("Enter the number of choice [1-5]: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                itemManager.add_item(item_id, name, description, price)
            except ValueError:
                print("Error! There was an invalid input.")
        elif choice == "2":
            itemManager.display_items()
        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID to update: "))
                name = input("Enter Updated Name: ") or None
                description = input("Enter Updated Description: ") or None
                price_input = input("Enter Updated Price: ")
                price = float(price_input) if price_input else None
                itemManager.update_item(item_id, name, description, price)
            except ValueError:
                print("Error! There was an invalid input.")
        elif choice == "4":
            try:
                item_id = int(input("Enter Item ID to delete: "))
                itemManager.delete_item(item_id)
            except ValueError:
                print("Error! There was an invalid input.")
        elif choice == "5":
            print("Program Exited.")
            break
        else:
            print("Invalid input! Please enter a valid choice.")

main()