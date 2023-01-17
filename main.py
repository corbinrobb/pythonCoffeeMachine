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
water = 300
milk = 200
coffee = 100
money = 0

user_input = input("What would you like? (espresso/latte/cappuccino) \n")

while user_input != "exit":
    if user_input == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        user_input = input("What would you like? (espresso/latte/cappuccino) \n")
        continue

    while user_input not in ["espresso", "latte", "cappuccino", "report"]:
        print(f"Sorry we do not have {user_input}")
        user_input = input("What would you like? (espresso/latte/cappuccino) \n")

    total = 0

    quarters = int(input("How many quarters?: "))
    total += quarters * 25

    dimes = int(input("How many dimes?: "))
    total += dimes * 10

    nickels = int(input("How many nickels?: "))
    total += nickels * 5

    pennies = int(input("How many pennies?: "))
    total += pennies

    total = round(total/100, 2)
    change = round(total - MENU[user_input]["cost"], 2)

    if MENU[user_input]["cost"] > total:
        print("Sorry, You do not have enough money")
    else:
        have_enough_ingredients = True
        drink_water = MENU[user_input]["ingredients"]["water"]
        drink_milk = MENU[user_input]["ingredients"]["milk"] if "milk" in MENU[user_input]["ingredients"] else 0
        drink_coffee = MENU[user_input]["ingredients"]["coffee"]

        if drink_water > water:
            print("Sorry, Not enough water")
            have_enough_ingredients = False

        if drink_milk > milk:
            print("Sorry, Not enough milk")
            have_enough_ingredients = False

        if drink_coffee > coffee:
            print("Sorry, Not enough coffee")
            have_enough_ingredients = False

        if have_enough_ingredients:
            water -= drink_water
            milk -= drink_milk
            coffee -= drink_coffee
            money += total - change

            print(f"Your change is ${change}")
            print(f"Here is your {user_input}")

    user_input = input("What would you like? (espresso/latte/cappuccino) \n")
