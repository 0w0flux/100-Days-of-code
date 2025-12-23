MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

euro = float(5)

def welcome():
    while True:
        try:
            choose = int(input("\nWhat would you like? \n1. Espresso \n2. Latte \n3. Cappuccino \n4. Report the required resources \n5. Report your resources \n6. Turn the machine off \n"))
            return choose
        except ValueError:
            print("\nInvalid input")

def check_resources(drink):
    print("")

    if "water" in drink:
        if drink["water"] > resources["water"]:
            print("Not enough resources...")
            return False

    if "coffee" in drink:
        if drink["coffee"] > resources["coffee"]:
            print("Not enough resources...")
            return False
    
    if "milk" in drink:
        if drink["milk"] > resources["milk"]:
            print("Not enough resources...")
            return False
    
    return True

def check_money(drink):

    if euro < drink:
        print("\nInsufficient funds!")
        return False
    else:
        return True

def main():
    global resources
    global euro

    while True:
        choose = welcome()
        if choose == 1:
            drink_resources = MENU["espresso"]["ingredients"]
            drink_price = MENU["espresso"]["cost"]

            if check_resources(drink_resources) == True:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                if check_money(drink_price) == True:
                    euro -= drink_price
                    print(f"Here is your espresso, you have {euro}€ left.")
            

        elif choose == 2:
            drink_resources = MENU["latte"]["ingredients"]
            drink_price = MENU["latte"]["cost"]

            if check_resources(drink_resources) == True:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                if check_money(drink_price) == True:
                    euro -= drink_price
                    print(f"Here is your latte, you have {euro}€ left.")

        elif choose == 3:
            drink_resources = MENU["cappuccino"]["ingredients"]
            drink_price = MENU["cappuccino"]["cost"]

            if check_resources(drink_resources) == True:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                if check_money(drink_price) == True:
                    euro -= drink_price
                    print(f"Here is your cappuccino, you have {euro}€ left.")

        elif choose == 4:
            print(f"Espresso:\n Water: {MENU['espresso']['ingredients']['water']}\n Coffee: {MENU['espresso']['ingredients']['coffee']}\n")
            print(f"Latte:\n Water: {MENU['latte']['ingredients']['water']}\n Coffee: {MENU['latte']['ingredients']['coffee']}\n Milk: {MENU['latte']['ingredients']['milk']}\n")
            print(f"Cappuccino:\n Water: {MENU['cappuccino']['ingredients']['water']}\n Coffee: {MENU['cappuccino']['ingredients']['coffee']}\n Milk: {MENU['cappuccino']['ingredients']['milk']}")

        elif choose == 5:
            print(f"\nYour resources: \n Money: {euro}€ \n Water: {resources['water']} \n Coffee: {resources['coffee']} \n Milk: {resources['milk']}")

        elif choose == 6:
            print("\nMachine is turning off.")
            break
        else:
            print("\nInvalid input")
        
if __name__ == "__main__":
    main()