import main
off = ""
while off != "off":
    print("Espresso- Latte - Cappuccino")
    user_choise = input("What would you like?: ")
    user_choise.lower()

    def user_input(coffee_name):
        if user_choise == "report":
            print(main.resources)
        elif user_choise == "off":
            global off
            off = "off"
        else:
            quarters = int(input("Enter quarters number: "))
            dimes = int(input("Enter dimes number: "))
            nickle = int(input("Enter nickle number: "))
            pennies = int(input("Enter pennies number: "))
            price_calculator(user_choise, quarters, dimes, nickle, pennies)


    def recipe(user_choise, price, money_in_machine=0):
        coffee_require = main.MENU[f"{user_choise}"]
        coffee_require1 = coffee_require["ingredients"]
        machine_resources = main.resources
        price_require = coffee_require["cost"]
        for i in coffee_require1:
            quantity = coffee_require1[i]
            resource_quantity = main.resources[i]
            left_quantity = resource_quantity - quantity
            main.resources[i] = left_quantity
            if price < price_require:
                print("Sorry that's not enough money. Money refunded.")
                break
            elif left_quantity <= 0:
                print(f"Sorry there is not enough {i}.")
                break
        surplus_money = price - price_require
        print("Please take the surplus money.")
        money_in_machine += price_require
        final(user_choise, money_in_machine)


    def final(user_choise, money):
        print(f"Here is your {user_choise}. We wait again :)))))")
        print(main.resources)
        print(f"Money in machine: {money}")

    def price_calculator(coffee, quarters, dimes, nickle, pennies):
        quarters *= 0.25
        dimes *= 0.10
        nickle *= 0.05
        pennies *= 0.01
        price = round(quarters + dimes + nickle + pennies, 2)
        recipe(coffee, price)


    user_input(user_choise)
