from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        order = input(f"\nChoose what you want: {menu.get_items()} \nReport (R) \nTurn the machine off (Q) \n").lower()
        if order == "report" or order == "r":
            print()
            coffee_maker.report()
            money_machine.report()
            print()

        elif order == "q":
            print("\nThanks for using the machine.")
            break

        elif menu.find_drink(order):
            item = menu.find_drink(order)

            if coffee_maker.is_resource_sufficient(item):
                
                if money_machine.make_payment(item.cost):                                                                                                                                                                                                 # payment.make_payment(item.cost)
                    coffee_maker.make_coffee(item)
                
                else:
                    print("\nInsufficient funds!")

            else:
                print("\nInsufficient resources!")

        else:
            continue
    

if __name__ == "__main__":
    main()