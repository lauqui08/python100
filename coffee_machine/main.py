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
money = 0


def total_payment():
    payment = [int(input("How many quarters: ")) * 0.25, int(input("How many dimes: ")) * 0.1,
               int(input("How many nickles: ")) * 0.05, int(input("How many pennies: ")) * 0.01]
    return sum(payment)


turn_on_machine = True
while True:

    options = input("What would you like? (espresso/latte/cappuccino): ")

    if options.lower() == "espresso":
        total_pay = total_payment()
        if total_pay >= MENU['espresso']['cost']:
            if MENU['espresso']['ingredients']['water'] > resources['water']:
                print(f"Insufficient water. You need to refill some water.")
            elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
                print(f"Insufficient coffee. You need to refill some coffee.")
            else:
                money += MENU['espresso']['cost']
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                if total_pay > MENU['espresso']['cost']:
                    print(f"Enjoy your coffee. Get your change: ${total_pay - MENU['espresso']['cost']}")
        else:
            print(f"Insufficient fund! Please try again.")

    elif options.lower() == "latte":
        total_pay = total_payment()
        if total_pay >= MENU['latte']['cost']:
            if MENU['latte']['ingredients']['water'] > resources['water']:
                print(f"Insufficient water. You need to refill some water.")
            elif MENU['latte']['ingredients']['coffee'] > resources['coffee']:
                print(f"Insufficient coffee. You need to refill some coffee.")
            elif MENU['latte']['ingredients']['milk'] > resources['milk']:
                print(f"Insufficient milk. You need to refill some milk.")
            else:
                money += MENU['latte']['cost']
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                if total_pay > MENU['latte']['cost']:
                    print(f"Enjoy your coffee. Get your change: ${total_pay - MENU['latte']['cost']}")
        else:
            print(f"Insufficient fund! Please try again.")
    elif options.lower() == "cappuccino":
        total_pay = total_payment()
        if total_pay >= MENU['cappuccino']['cost']:
            if MENU['cappuccino']['ingredients']['water'] > resources['water']:
                print(f"Insufficient water. You need to refill some water.")
            elif MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']:
                print(f"Insufficient coffee. You need to refill some coffee.")
            elif MENU['cappuccino']['ingredients']['milk'] > resources['milk']:
                print(f"Insufficient milk. You need to refill some milk.")
            else:
                money += MENU['cappuccino']['cost']
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                if total_pay > MENU['cappuccino']['cost']:
                    print(f"Enjoy your coffee. Get your change: ${total_pay - MENU['cappuccino']['cost']}")
        else:
            print(f"Insufficient fund! Please try again.")
    elif options.lower() == "report":
        print(f"Total Money: {money}")
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
    elif options.lower() == "off":
        turn_on_machine = False
    elif options.lower() == "refill":
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
    else:
        print(f"Invalid input please try again!")
