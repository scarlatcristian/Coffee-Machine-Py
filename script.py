from coffee import coffee_type

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


def add_more_resources(coffee_machine, coffee):
    if coffee_machine["water"] < coffee["water"]:
        coffee_machine["water"] += int(
            input("How many ml of water you want to add?: "))

    if coffee_machine["milk"] < coffee["milk"]:
        coffee_machine["milk"] += int(
            input("How many ml of milk you want to add?: "))

    if coffee_machine["coffee"] < coffee["coffee"]:
        coffee_machine["coffee"] += int(
            input("How many g of coffee you want to add?: "))
    return coffee_machine


def making_coffee(coffee_machine, coffee):
    coffee_machine["water"] -= coffee["water"]
    coffee_machine["milk"] -= coffee["milk"]
    coffee_machine["coffee"] -= coffee["coffee"]
    coffee_machine["money"] += coffee["price"]
    return coffee_machine


def pay_coffee():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = coins["quarter"] * quarters + coins["dime"] * \
        dimes + coins["nickel"] * nickles + coins["penny"] * pennies
    return total


def check_coffee_machine(coffee_machine):
    for key in coffee_machine:
        if key == 'water' or key == 'milk':
            print(f"{key.capitalize()}: {coffee_machine[key]}ml")
        elif key == 'coffee':
            print(f"{key.capitalize()}: {coffee_machine[key]}g")
        elif key == 'money':
            print(f"{key.capitalize()}: {coffee_machine[key]}$")


def check_if_costumer():
    answer = input("Would you like a coffee? Type y/n: ").lower()
    if answer == 'y' or answer == 'yes':
        return True
    else:
        return False


def can_machine_make_coffee(coffee_machine, coffee):
    """
    Will return true if the machine has enough ingredients to make coffee, otherwise it will return false
    """
    if coffee["water"] > coffee_machine["water"] or coffee["milk"] > coffee_machine["milk"] or coffee["coffee"] > coffee_machine["coffee"]:
        if coffee["water"] > coffee_machine["water"]:
            print(
                f"Sorry not enough water. Only {coffee_machine['water']}ml left and needed {coffee['water']}ml for the coffee")
        if coffee["milk"] > coffee_machine["milk"]:
            print(
                f"Sorry not enough milk. Only {coffee_machine['milk']}ml left and needed {coffee['milk']}ml for the coffee")
        if coffee["coffee"] > coffee_machine["coffee"]:
            print(
                f"Sorry not enough coffee. Only {coffee_machine['coffee']}ml left and needed {coffee['coffee']}ml for the coffee")
        return False
    return True


def coffee_machine():
    coffee_machine = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    machine_on = True
    while machine_on:
        coffee_name = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        while coffee_name != 'espresso' and coffee_name != 'latte' and coffee_name != 'cappuccino' and coffee_name != 'report' and coffee_name != 'off':
            coffee_name = input(
                "Enter a valid option (espresso/latte/cappuccino): ").lower()

        if coffee_name == 'report':
            check_coffee_machine(coffee_machine)

        if coffee_name == 'off':
            machine_on = False

        else:
            coffee_choice = coffee_type[coffee_name]
            coffee_price = coffee_choice["price"]
            coffee_has_resources = can_machine_make_coffee(
                coffee_machine, coffee_choice)

            while not coffee_has_resources:
                coffee_machine = add_more_resources(
                    coffee_machine, coffee_choice)
                coffee_has_resources = can_machine_make_coffee(
                    coffee_machine=coffee_machine, coffee=coffee_choice)

            print(
                f"The price for the {coffee_name} is {coffee_price}$")

            total = pay_coffee()

            return_money = False
            while total < coffee_price and return_money == False:
                print(f"{coffee_price - total}$ left to pay")

                return_money = input(
                    "Type 'y' to return the money or 'n' to add more? Type y/n: ").lower()

                if return_money == 'y' or return_money == 'yes':
                    print(f"Here is your money back {total}$")
                    return_money = True
                else:
                    print(f"{coffee_price - total}$ left to pay")
                    left_to_pay = pay_coffee()
                    total += left_to_pay
                    if total < coffee_price:
                        return_money = False

            if total > coffee_price:
                print(f"Here is {total - coffee_price}$ in change")

                coffee_machine = making_coffee(coffee_machine, coffee_choice)
                print(f"Here is your {coffee_name}. Enjoy!")

        return_money = False


coffee_machine()
