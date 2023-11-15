from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
money = MoneyMachine()
menu_attributes = MenuItem
coffee_made = CoffeeMaker()
checker = True
while checker:
    print(menu.get_items())
    user_drink = menu.find_drink(input("What would you like: "))
    if user_drink is not None:
        if money.make_payment(user_drink.cost):
            if coffee_made.is_resource_sufficient(user_drink):
                coffee_made.make_coffee(user_drink)
    elif user_drink is None:
        coffee_made.report()
        money.report()
