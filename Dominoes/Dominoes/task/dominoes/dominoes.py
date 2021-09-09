# Write your code here
import random
from collections import namedtuple
Dominoes = namedtuple('Dominoes', ['stock', 'computer', 'player', 'snake'])


def main_menu():
    piles = None
    setup = 'shuffle'
    while setup == 'shuffle':
        game_pieces = create_dominoes()
        piles = deal(game_pieces)
        setup = start(piles)
    status = init(piles, setup)
    while True:
        if game_state(piles, status):
            break
        turn(piles, status)
        status = switch_turns(status)


def create_dominoes():
    dominoes = []
    pool = [x for x in range(7)]
    master = pool[:]
    for i in pool:
        for j in master:
            dominoes.append([i, j])
        master.pop(0)
    return dominoes


def deal(game_pieces):
    stock = []
    computer = []
    player = []
    snake = []
    for i in [stock, computer, player, stock]:
        for _ in range(7):
            current = random.choice(game_pieces)
            game_pieces.remove(current)
            i.append(current)
    return Dominoes(stock, computer, player, snake)


def start(piles):
    for i in range(6, -1, -1):
        if [i, i] in piles[1]:
            return 'computer', [i, i]
        if [i, i] in piles[2]:
            return 'player', [i, i]
    else:
        return 'shuffle'


def init(piles, setup):
    if setup[0] == 'computer':
        piles.computer.remove(setup[1])
        piles.snake.append(setup[1])
        return 'player'
    if setup[0] == 'player':
        piles.player.remove(setup[1])
        piles.snake.append(setup[1])
        return 'computer'


def game_state(piles, status):
    display(piles)
    if check(piles, status):
        return True
    else:
        if status == 'computer':
            print('Status: Computer is about to make a move. Press Enter to continue...')
        elif status == 'player':
            print('Status: It\'s your turn to make a move. Enter your command.')
        return False


def display(piles):
    print('=' * 70)
    print(f'Stock size: {len(piles.stock)}')
    print(f'Computer pieces: {len(piles.computer)}')
    print()
    game_field = ''
    if len(piles.snake) < 6:
        for i in piles.snake:
            game_field += str(i)
    else:
        for i in piles.snake[:3]:
            game_field += str(i)
        game_field += '...'
        for i in piles.snake[-3:]:
            game_field += str(i)
    print(game_field)
    print()
    print('Your pieces:')
    for i, j in enumerate(piles.player):
        print(f'{i+1}:{j}')
    print()


def check(piles, status):
    if not piles.computer:
        print('Status: The game is over. The computer won!')
        return True
    elif not piles.player:
        print('Status: The game is over. You won!')
        return True
    elif check_draw(piles):
        print('Status: The game is over. It\'s a draw!')
        return True
    elif not piles.stock:
        if not no_stock(piles, 'computer'):
            print('Status: The game is over. It\'s a draw!')
            return True
        elif not no_stock(piles, 'player'):
            print('Status: The game is over. It\'s a draw!')
            return True
        else:
            print('Status: The game is over. It\'s a draw!')
            return True
    return False


def check_draw(piles):
    for i in [x for x in range(7)]:
        count = 0
        for j in piles.snake:
            if i in j:
                count += 1
        if count == 8:
            return True


def turn(piles, status):
    if status == 'computer':
        while True:
            user = input()
            if not user:
                break
        order = algorithm(piles)
        while True:
            if order:
                index = order.index(max(order))
                if process_turn(piles, index+1, status):
                    break
                order.pop(index)
            else:
                if process_turn(piles, 0, status):
                    break
    elif status == 'player':
        while True:
            try:
                user = int(input())
            except ValueError:
                print('Invalid input. Please try again.')
            else:
                if 0 - len(piles.player) <= user <= len(piles.player):
                    if process_turn(piles, user, status):
                        break
                    else:
                        print('Illegal move. Please try again.')
                else:
                    print('Invalid input. Please try again.')


def algorithm(piles):
    order = []
    count = {x: 0 for x in range(7)}
    for i in {x for x in range(7)}:
        for j in [piles.computer, piles.snake]:
            for k in j:
                if i in k:
                    count[i] += 1
    for i in piles.computer:
        order.append(count[i[0]] + count[i[1]])
    return order


def process_turn(piles, user, status):
    current = None
    if status == 'computer':
        current = piles.computer
    elif status == 'player':
        current = piles.player
    if user == 0:
        if piles.stock:
            selected = random.randint(0, len(piles.stock) - 1)
            selected = piles.stock.pop(selected)
            current.append(selected)
        else:
            return False
    else:
        piece = current[abs(user) - 1]
        rules = valid_move(piles, piece)
        if rules:
            if not rules[1]:
                piece = flip(piece)
        else:
            return False
        if rules[2] == 'left':
            piles.snake.insert(0, piece)
            current.pop(abs(user) - 1)
        elif rules[2] == 'right':
            piles.snake.append(piece)
            current.pop(abs(user) - 1)
    return True


def valid_move(piles, piece):
    if piece[1] == piles.snake[0][0]:
        return True, True, 'left'
    elif piece[0] == piles.snake[-1][-1]:
        return True, True, 'right'
    elif piece[0] == piles.snake[0][0]:
        return True, False, 'left'
    elif piece[1] == piles.snake[-1][-1]:
        return True, False, 'right'
    else:
        return False


def flip(piece):
    return [piece[1], piece[0]]


def no_stock(piles, status):
    possible = False
    current = None
    if status == 'computer':
        current = piles.computer
    elif status == 'player':
        current = piles.player
    for i in current:
        if valid_move(piles, i):
            possible = True
    return possible


def switch_turns(status):
    if status == 'computer':
        return 'player'
    elif status == 'player':
        return 'computer'


main_menu()
