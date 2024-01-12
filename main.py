
print("Welcome to Pizza Time!")
print("Select an option below: ")
print("")
print("1. Order")
print("2. Checkout")
print("3. Inventory")
print("4. Exit")
print("")

import order
import checkout
import inventory

while True:
    selection = input(">> ")

    if selection == "1":
        order.orderstart()

    elif selection == "2":
        checkout.checkoutstart()

    elif selection == "3":
        inventory.inventorystart()

    elif selection == "4":
        print("Goodbye!")
        break

    else:
        print("Please enter the correct number for the option you want")