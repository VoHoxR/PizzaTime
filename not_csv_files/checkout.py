def checkoutstart(order):
    subtotal = 0
    tax_rate = 0.095
    print("Customer Order:")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price

    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax)
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Total: $" + str(total))

    payment(total)
    save(order, total)

    input("(Press ENTER to continue):)")

    print("this is the checkout system")

def payment(total):
    while True:
        payment_type = input ("Cash or reddit gold? ")
        if payment_type.lower() == "cash":
            print(f"The total is ${total}")
            cash = int(input("Enter cash recieved: "))
            if cash >= total:
                change = cash - total
                print(f"Return ${change} to the customer.")
                input("(Press ENTER to continue)")
                break
            else:
                print(f"That is not enough.")
                continue
            

        elif payment_type.lower() == "reddit gold":
            print(f"The total is {round(total, 1)} reddit gold")
            input("(Press ENTER to give us your reddit gold)")
            break
        else:
            print("That is not a valid currency")

def save(order, total):
    with open("pizza.dat", "a") as orders:
        for pizza in order:
            orders.write(f" {pizza.quantity} {pizza.size} {pizza.type} | ${pizza.price} | ${total} \n\n")
