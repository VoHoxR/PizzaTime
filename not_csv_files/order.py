import pandas, warnings

class Order:
    def __init__(self, quantity, size, type, price):
        self.quantity = quantity
        self.size = size
        self.type = type
        self.price = float(price[1:])

warnings.simplefilter(action='ignore', category=FutureWarning)

def orderstart():

    print(""" 
                 Pizzas
--------------------------------------""")
    
    order = []
    while True:
        pizza_menu = pandas.read_csv("csv_files/types.csv")
        print(pizza_menu[["Type", "Size", "Price"]])
        print("\n What would you like? \n")

        selection = int(input(">> "))
        if selection > len(pizza_menu)-1:
            print("Please choose an available type.")
            continue

        size = pizza_menu.iloc[selection][1]
        ptype = pizza_menu.iloc[selection][0]
        price = pizza_menu.iloc[selection][2]
        quantity = int(input(f"How many {size} {ptype} pizzas do you want? "))

        order.append(Order(quantity, size, ptype, price))

        print("Would you like to order another pizza? (y/n) ")
        confirm = input(">> ")
        
        if confirm.lower() == "y":
            continue
        else:
            break

    for i in order:
        print(f"{i.quantity} {i.size} {i.type} pizzas | {i.price} each")

    return order