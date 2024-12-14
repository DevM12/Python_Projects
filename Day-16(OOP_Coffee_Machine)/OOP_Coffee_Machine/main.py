from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffee_machine():
    repeat = True
    while repeat:
        menu_items = menu.get_items()
        user_choice = input(f'What would you like? ({menu_items}):').strip().lower()
        if user_choice in menu_items:
            drink = menu.find_drink(user_choice)
            if drink and coffee_maker.is_resource_sufficient(drink):

                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        elif user_choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif user_choice == 'off':
            repeat = False
            print("Turning off the coffee machine. Goodbye!")
        else:
            print('Enter a valid input')


coffee_machine()