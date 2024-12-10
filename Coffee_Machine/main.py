from directories import MENU,resources
def coffee_machine():
    def coffee_details(user_action):
        coffee = MENU[user_action]
        mrp=coffee['cost']
        ingredients=coffee['ingredients']
        return [mrp,ingredients]
    def calculate_change(mrp):
        print('Please insert coins.')
        def get_coin_input(coin_name, coin_value):
            while True:
                try:
                    coin_count = float(input(f'How many {coin_name}?: '))
                    if coin_count < 0:
                        raise ValueError("Negative values are not allowed.")
                    return coin_count * coin_value
                except ValueError:
                    print(f"Invalid input for {coin_name}. Please enter a valid number.")

        quarters = get_coin_input("quarters", 0.25)
        dimes = get_coin_input("dimes", 0.10)
        nickels = get_coin_input("nickels", 0.05)
        pennies = get_coin_input("pennies", 0.01)

        received_value = quarters + dimes + nickels + pennies
        total_change = round(received_value - mrp, 2)

        if total_change < 0:
            print("Not enough money. Please insert more coins.")
            return calculate_change(mrp)  # Recursive call for insufficient payment
        else:
            return total_change
    def resources_remaining(ingredients,total_resources):
        for item, amount in ingredients.items():
            total_resources[item] -= amount
        return [
            total_resources.get('water', 0),
            total_resources.get('coffee', 0),
            total_resources.get('milk', 0)
        ]
    def resources_availability(water, coffee, milk):
        if water<0 or coffee<0 or milk<0:
            return False
        else:
            return True
    def reclaim_resources(ingredients,total_resources):
        for item, amount in ingredients.items():
            total_resources[item] += amount
    shutdown=False
    while not shutdown:
        action = input('What would you like? (espresso,latte,cappuccino): ').lower()
        if action=='report':
            print(f'Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']}')
        elif action=='shutdown':
            shutdown=True
            return shutdown
        elif action in MENU:
            [coffee_mrp,coffee_ingredients]=coffee_details(action)
            [water_remaining, coffee_remaining, milk_remaining] = resources_remaining(coffee_ingredients, resources)
            enough_resources=resources_availability(water_remaining, coffee_remaining, milk_remaining)
            if enough_resources:
                change=calculate_change(coffee_mrp)
                print(f'Your total change is: {change} \nHere is your {action} ☕. Enjoy!')
            else:
                print('Not enough resources')
                reclaim_resources(coffee_ingredients, resources)
        else:
            print('Enter a valid input')

coffee_machine()