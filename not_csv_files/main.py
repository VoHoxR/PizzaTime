


from os import system
import order,checkout,inventory

cust_order = []
while True:
    print("")
    print("Welcome to Pizza Time!")
    print("Select an option below: ")
    print("----------")
    print("1. Order")
    print("2. Checkout")
    print("3. Inventory")
    print("4. Exit")
    print("")

    selection = input(">> ")

    if selection == "1":
        cust_order = customer_order = order.orderstart()
    elif selection == "2":
        if len(customer_order) > 0:
            checkout.checkoutstart(cust_order)
        else:
            print("The cart is empty")

    elif selection == "3":
        inventory.inventorystart()

    elif selection == "4":
        print("Goodbye!")
        

    else:
        print("Please enter the correct number for the option you want")

    system("cls")