# Write your code here
class CoffeeMachine:
    current_money = 550
    current_water = 400
    current_milk = 540
    current_beans = 120
    current_cups = 9
    fill_order = []

    def __init__(self):
        self.state = ''
        self.fill_state = 'water'
        self.pre_main_menu()

    def pre_main_menu(self):
        self.state = 'main_menu'
        print('Write action (buy, fill, take, remaining, exit):')

    def main_menu(self, user_input):
        if user_input == 'buy':
            self.pre_buy_menu()
        elif user_input == 'fill':
            self.pre_fill_menu()
        elif user_input == 'take':
            self.take()
            self.pre_main_menu()
        elif user_input == 'remaining':
            self.remaining()
            self.pre_main_menu()
        elif user_input == 'exit':
            pass
        return user_input

    def pre_buy_menu(self):
        self.state = 'buy_menu'
        print()
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

    def buy_menu(self, user_input):
        def espresso():
            needed_water = 250
            needed_milk = 0
            needed_beans = 16
            cost = 4
            if self.ping(needed_water, needed_milk, needed_beans):
                self.update(cost, needed_water, needed_milk, needed_beans, 1, 'buy')

        def latte():
            needed_water = 350
            needed_milk = 75
            needed_beans = 20
            cost = 7
            if self.ping(needed_water, needed_milk, needed_beans):
                self.update(cost, needed_water, needed_milk, needed_beans, 1, 'buy')

        def cappuccino():
            needed_water = 200
            needed_milk = 100
            needed_beans = 12
            cost = 6
            if self.ping(needed_water, needed_milk, needed_beans):
                self.update(cost, needed_water, needed_milk, needed_beans, 1, 'buy')

        if user_input == '1':
            espresso()
            self.pre_main_menu()
        elif user_input == '2':
            latte()
            self.pre_main_menu()
        elif user_input == '3':
            cappuccino()
            self.pre_main_menu()
        elif user_input == 'back':
            self.pre_main_menu()
        return user_input

    def pre_fill_menu(self):
        self.state = 'fill_menu'
        if self.fill_state == 'water':
            print()
            print('Write how many ml of water you want to add:')
        elif self.fill_state == 'milk':
            print('Write how many ml of milk you want to add:')
        elif self.fill_state == 'beans':
            print('Write how many grams of coffee beans you want to add:')
        elif self.fill_state == 'cups':
            print('Write how many disposable coffee cups you want to add:')

    def fill_menu(self, user_input):
        if self.fill_state == 'water':
            self.fill_order.append(user_input)
            self.fill_state = 'milk'
            self.pre_fill_menu()
        elif self.fill_state == 'milk':
            self.fill_order.append(user_input)
            self.fill_state = 'beans'
            self.pre_fill_menu()
        elif self.fill_state == 'beans':
            self.fill_order.append(user_input)
            self.fill_state = 'cups'
            self.pre_fill_menu()
        elif self.fill_state == 'cups':
            self.fill_order.append(user_input)
            self.fill_state = 'water'

            added_water = int(self.fill_order[0])
            added_milk = int(self.fill_order[1])
            added_beans = int(self.fill_order[2])
            added_cups = int(self.fill_order[3])
            self.update(0, added_water, added_milk, added_beans, added_cups, 'fill')
            self.fill_order.clear()
            print()

            self.pre_main_menu()
        return user_input

    def take(self):
        print()
        print(f'I gave you ${self.current_money}')
        print()
        self.update(0, 0, 0, 0, 0, 'take')

    def remaining(self):
        print()
        print('The coffee machine has')
        print(f'{self.current_water} of water')
        print(f'{self.current_milk} of milk')
        print(f'{self.current_beans} of beans')
        print(f'{self.current_cups} of disposable cups')
        print(f'${self.current_money} of money')
        print()

    def ping(self, water, milk, beans):
        if water <= self.current_water:
            if milk <= self.current_milk:
                if beans <= self.current_beans:
                    if 1 <= self.current_cups:
                        print('I have enough resources, making you a coffee!')
                        print()
                        return True
                    else:
                        print('Sorry, not enough cups!')
                        print()
                        return False
                else:
                    print('Sorry, not enough beans!')
                    print()
                    return False
            else:
                print('Sorry, not enough milk!')
                print()
                return False
        else:
            print('Sorry, not enough water!')
            print()
            return False

    def update(self, money, water, milk, beans, cups, action):
        if action == 'buy':
            self.current_money += money
            self.current_water -= water
            self.current_milk -= milk
            self.current_beans -= beans
            self.current_cups -= cups
        elif action == 'fill':
            self.current_water += water
            self.current_milk += milk
            self.current_beans += beans
            self.current_cups += cups
        elif action == 'take':
            self.current_money = 0

    def user(self, user_input):
        if self.state == 'main_menu':
            return self.main_menu(user_input)
        elif self.state == 'buy_menu':
            return self.buy_menu(user_input)
        elif self.state == 'fill_menu':
            return self.fill_menu(user_input)


coffee_machine = CoffeeMachine()
while True:
    user = input()
    output = coffee_machine.user(user)
    if output == 'exit':
        break
