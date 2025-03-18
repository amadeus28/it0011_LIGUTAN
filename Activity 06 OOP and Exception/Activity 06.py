class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
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

class ItemManager:
    def __init__(self):
        self.items = {}
    
    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Item ID already exists.")
            return
        try:
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print("Error: " + str(e))
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print("ID:", item.id, "Name:", item.name, "Description:", item.description, "Price: $", round(item.price, 2))
    
    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Item ID not found.")
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
            print("Item ID not found.")

def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                description = input("Enter Description: ")
                price = float(input("Enter Price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input! Please enter valid values.")
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID to update: "))
                name = input("Enter new Name (leave blank to keep current): ")
                description = input("Enter new Description (leave blank to keep current): ")
                price_input = input("Enter new Price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name or None, description or None, price)
            except ValueError:
                print("Invalid input! Please enter valid values.")
        elif choice == "4":
            try:
                item_id = int(input("Enter Item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input! Please enter a valid ID.")
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
