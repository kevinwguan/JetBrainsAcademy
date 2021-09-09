# write your code here
def main_menu():
    turn_dict = init()
    while True:
        turn(turn_dict)
        state_print(dict_to_string(turn_dict))
        if check(dict_to_string(turn_dict)):
            break
        else:
            switch()


def init():
    state = ' ' * 9
    state_print(state)
    return valid(state)


def state_print(game_state):
    vertical_border = '-' * 9
    horizontal_border = '|' + ' '
    three_lines = [horizontal_border for i in range(3)]
    for i in range(len(game_state)):
        if i < 3:
            three_lines[0] += game_state[i]
            three_lines[0] += ' '
        elif i < 6:
            three_lines[1] += game_state[i]
            three_lines[1] += ' '
        elif i < 9:
            three_lines[2] += game_state[i]
            three_lines[2] += ' '
    for i in range(3):
        three_lines[i] += '|'
    print(vertical_border)
    print(three_lines[0])
    print(three_lines[1])
    print(three_lines[2])
    print(vertical_border)


def check(game_state):
    if winner(game_state, 'XXX'):
        print('X wins')
        return True
    elif winner(game_state, 'OOO'):
        print('O wins')
        return True
    elif game_state.count(' ') == 0:
        print('Draw')
        return True
    else:
        return False


def winner(game_state, player):
    for i in range(3):
        if game_state[i*3:i*3+3] == player:
            return True
        elif game_state[i::3] == player:
            return True
    else:
        if game_state[::4] == player:
            return True
        if game_state[2:7:2] == player:
            return True
    return False


def valid(game_state):
    index = 0
    valid_dict = {}
    for x in range(1, 4):
        for y in range(1, 4):
            valid_dict[(x, y)] = game_state[index]
            index += 1
    return valid_dict


def turn(valid_dict):
    while True:
        try:
            x, y = input('Enter the coordinates: ').split()
            x = int(x)
            y = int(y)
        except ValueError:
            print('You should enter numbers!')
        else:
            coordinates = (x, y)
            for i in coordinates:
                if not (1 <= i <= 3):
                    print('Coordinates should be from 1 to 3!')
                    break
            else:
                if valid_dict[coordinates] == 'X' or valid_dict[coordinates] == 'O':
                    print('This cell is occupied! Choose another one!')
                elif valid_dict[coordinates] == ' ':
                    valid_dict[coordinates] = user
                    break


def switch():
    global user
    if user == 'X':
        user = 'O'
    elif user == 'O':
        user = 'X'


def dict_to_string(valid_dict):
    state = ''
    for x in range(1, 4):
        for y in range(1, 4):
            state += valid_dict[(x, y)]
    return state


user = 'X'
main_menu()
