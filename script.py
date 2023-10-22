from coffee import coffees

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


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


def make_coffee(coffee_machine, coffee):
    """
    Will return true if the machine has enough ingredients to make coffee, otherwise it will return false
    """
    if coffee["water"] > coffee_machine["water"]:
        print("Sorry no enough water.")
        return False
    if coffee["milk"] > coffee_machine["milk"]:
        print("Sorry no enough milk.")
        return False
    if coffee["coffee"] > coffee_machine["coffee"]:
        print("Sorry no enough coffee.")
        return False
    return True


def coffee_machine():
    coffee_machine = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    coffee_choice = ''

    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    while choice != 'espresso' and choice != 'latte' and choice != 'cappuccino' and choice != 'report':
        choice = input(
            "Enter a valid option (espresso/latte/cappuccino): ").lower()

    if choice == 'report':
        check_coffee_machine(coffee_machine)
    else:
        coffee_choice = coffees[choice]

    making_coffee = make_coffee(
        coffee_machine=coffee_machine, coffee=coffee_choice)

    if making_coffee:
        print(
            f"The price for the {choice} is {coffee_choice['price']}$")
        total = pay_coffee()

        while total < coffee_choice["price"]:
            print(f"{coffee_choice['price'] - total}$ left to pay")
            left_to_pay = pay_coffee()
            total += left_to_pay

        if total > coffee_choice["price"]:
            print(f"Here is {total- coffee_choice['price']}$ in change")


coffee_machine()
