#Day 15 Project: Coffe Machine

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# Variables
order = ""
machine_money = 0
payment = 0.0
change = 0.0
should_continue = True

# Machine loop
while should_continue:

    # 1) Asking the order

    order = ""
    while not (order == "espresso" or order == "latte" or order == "cappuccino" or order == "report" or order == "exit"):
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # 2) Report option - shows the administrator how much resources the machine has

    if order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffe: {resources['coffee']}g\nMoney: ${machine_money}\n")
        continue

    if order == "exit":
        break


    # 3) Payment - Receive the coins from the client and calculate his payment

    print(f"You choose {order}, cost ${menu[order]["cost"]}\nPlease insert coins: ")
    payment = float(input("How many Penny's"))/100
    payment += 5 * (float(input("How many Nickel's"))/100)
    payment += 10 * (float(input("How many Dime's"))/100)
    payment += 25 * (float(input("How many Quarter's"))/100)
    payment = round(payment, 2)
    print(f"You have paid: ${payment}")

    # 4) Return to the client his order if the machine has enough resources and if he payed enough money, giving him his change. 
        
    if payment >= menu[order]['cost'] and resources["coffee"] >= menu[order]["ingredients"]["coffee"] and resources["milk"] >= menu[order]["ingredients"]["milk"] and resources["water"] >= menu[order]["ingredients"]["water"]:
        change = round(payment - menu[order]['cost'], 2) 
        print(f"Here is ${change} in change\nHere is your {order}! Enjoy :)")
        machine_money += round(payment - change, 2)
        resources["coffee"] -= menu[order]["ingredients"]["coffee"]
        resources["milk"] -= menu[order]["ingredients"]["milk"]
        resources["water"] -= menu[order]["ingredients"]["water"]

    elif payment < menu[order]['cost']:
        print("Sorry that's not enough money. Money refunded")
    else: 
        print("Sorry, the machine was not enough resources to complet your order.")



