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

# Starting values
resources = {"water": 300,
             "milk": 200,
             "coffee": 150,
             "money": 0}


is_running = True

while is_running:
    user_input = input("What would you like? (espresso/latte/cappuccino) \n")

    if user_input == "off":
        is_running = False
        continue

    if user_input not in ["espresso", "latte", "cappuccino", "report"]:
        print(f"Sorry we do not have {user_input}")
        continue

    if user_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        continue

    total = 0

    quarters = int(input("How many quarters?: "))
    total += quarters * 25

    dimes = int(input("How many dimes?: "))
    total += dimes * 10

    nickels = int(input("How many nickels?: "))
    total += nickels * 5

    pennies = int(input("How many pennies?: "))
    total += pennies

    total = round(total / 100, 2)
    change = round(total - MENU[user_input]["cost"], 2)

    if MENU[user_input]["cost"] > total:
        print("Sorry, You do not have enough money")
    else:
        have_enough_ingredients = True

        for ingredient in (MENU[user_input]["ingredients"].keys()):
            ingredient_amount = MENU[user_input]["ingredients"][ingredient]
            if ingredient_amount > resources[ingredient]:
                print(f"Sorry, Not enough {ingredient}")
                have_enough_ingredients = False
                continue
            else:
                resources[ingredient] -= ingredient_amount

        if have_enough_ingredients:
            resources["money"] += round(total - change, 2)

            print(f"Your change is ${change}")
            print(f"Here is your {user_input}")
