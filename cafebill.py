#Cafe Billing application using Python
#cafebill.py
menu = {"pizza":450,
        "Burger":200,
        "Sandwich":130,
        "Cold Coffe":100,
        "Hot Coffe":120
        }
#Tax rate (in percentage)
tax_rate = 5.5 #5.5% tax
#service charge rate (in percentage)
service_charge_rate = 10.0 # 10.0% service charge
#discount
discount_rate=5.0 #5.0% discount
#Empty order Dictionery(item,price)
order = {}
def display_menu():
    print("Menu:")
    for item,price in menu.items():
        print(f"{item}:{price} Rs")

def add_to_order():
    item = input("Enter item to add:")
    if item in menu:
        quantity = int(input("Enter quantity of {item}:"))
        if item in order:
            order[item] +=quantity
        else:
            order[item] = quantity
            print(f"{quantity} {item}(s) added to the order.")
    else:
        print("Item not found in the menu.")


def calculate_total():
    subtotal = sum(menu[item] * quantity for item,quantity in order.items())
    tax =(tax_rate /100)*subtotal
    service_charge =(service_charge_rate /100)*subtotal
    total =subtotal + tax +   service_charge
    discount=(discount_rate/100)*total
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax ({tax_rate}%): {tax:.2f}")
    print(f"Service Charge ({service_charge_rate}%): {service_charge:.2f}")
    print(f"Discount ({discount_rate}%): {discount:.2f}")
    final_total= total - discount
    print(f"Total: RS{final_total:.2f}",)


print("\nCAFE BILLING APPLICATION")
print("1.Display Menu")
print("2.Add to Order")
print("3.Calculator Total")
print("4.Quit")
while(True):

    choice =input("Enter your choice:")

    if choice == "1":
            display_menu()
    elif choice == "2":
            add_to_order()
    elif choice == "3":
            calculate_total()

    elif choice == "4":
        print("Thanks for coming!!")
        break

    else:
        print("Invalid choice, please choose a valid option.")
