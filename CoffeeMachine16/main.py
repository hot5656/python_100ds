# Dictionary
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
profile = 0


def check_source(coffee, source):
    lack = ""
    print(f'{coffee}')
    # print(f'{source}')

    for item in coffee["ingredients"]:
        if source["water"] < coffee["ingredients"]["water"]:
            lack = item
            break

    # if source["water"] < coffee["ingredients"]["water"]:
    #     lack = "water"
    # elif source["coffee"] < coffee["ingredients"]["coffee"]:
    #     lack = "coffee"
    #
    # if "milk" in coffee["ingredients"]:
    #     if source["milk"] < coffee["ingredients"]["milk"]:
    #         lack = "milk"

    if lack != "":
        print(f'    Sorry there in not enough {lack}')
        return False
    else:
        return True


def insert_coin(cost):
    """ check coin """
    insert_money = 0
    # coin = float(input('    How many quarters?:'))
    print("Please insert coins.")
    coin = int(input('    How many quarters?:'))
    insert_money += coin*0.25
    coin = int(input('    How many dimes?:'))
    insert_money += coin*0.1
    coin = int(input('    How many nickles?:'))
    insert_money += coin*0.05
    coin = int(input('    How many pennies?:'))
    insert_money += coin*0.01
    print(f'    money= ${insert_money:.2f}, cost= ${cost}')
    if insert_money < cost:
        print(f'    Sorry that\'s not enough money. Money return')
        return 0
    else:
        print(f'    Here is ${round(insert_money-cost,2)} in charge.')
    return cost


def make_coff(coffee, money):
    global profile
    for item in coffee["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    profile += money


while True:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice in MENU:
        # TODO: 2. check resource sufficient
        if check_source(MENU[choice], resources):
            # TODO: 3. process coins
            get_money = insert_coin(MENU[choice]["cost"])
            if get_money > 0:
                # TODO: 4. check transaction successful
                # TODO: 5. make coffee
                # resources["water"] -= MENU[choice]["ingredients"]["water"]
                # resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                # profile += get_money
                # if "milk" in MENU[choice]["ingredients"]:
                #     resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                # for item in MENU[choice]["ingredients"]:
                #     resources[item] -= MENU[choice]["ingredients"][item]
                make_coff(MENU[choice], get_money)
                print(f'    Hear is your {choice} ☕ Enjoy')
    elif choice == "report":
        # TODO: 1. print report
        print(f'    Water : {resources["water"]}ml')
        print(f'    Milk  : {resources["milk"]}ml')
        print(f'    Coffee: {resources["coffee"]}ml')
        print(f'    Money : ${profile} ')
    elif choice == "off":
        break
    else:
        print('input error')