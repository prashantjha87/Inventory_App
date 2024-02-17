# inventory.py

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity, price):
        if product_id not in self.products:
            self.products[product_id] = {'name': name, 'quantity': quantity, 'price': price}
            print(f"Product '{name}' added to inventory.")
        else:
            print(f"Product with ID {product_id} already exists in inventory.")

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.products:
            self.products[product_id]['quantity'] = new_quantity
            print(f"Quantity updated for product ID {product_id}.")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        print("ID | Name | Quantity | Price")
        print("-" * 30)
        for product_id, details in self.products.items():
            print(f"{product_id} | {details['name']} | {details['quantity']} | ${details['price']:.2f}")
        print("-" * 30)
