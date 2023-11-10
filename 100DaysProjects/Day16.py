#Day 16 Project: Coffe Machine using OOP (Object Oriented Programing)

from Extra_Data.Data16.menu import Menu
from Extra_Data.Data16.coffee_maker import CoffeeMaker
from Extra_Data.Data16.money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and (money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)