# main.py
from inventory import Inventory

if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("\n1. Add Product\n2. Update Quantity\n3. Display Inventory\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            inventory.add_product(product_id, name, quantity, price)

        elif choice == '2':
            product_id = input("Enter product ID to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(product_id, new_quantity)

        elif choice == '3':
            inventory.display_inventory()

        elif choice == '4':
            print("Exiting the inventory application.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
