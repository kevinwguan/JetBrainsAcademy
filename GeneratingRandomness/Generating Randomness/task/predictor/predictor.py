import random


def init():
    string = ''
    print('Please give AI some data to learn...')
    while len(string) < 100:
        print(f'The current data length is {len(string)}, {100 - len(string)} symbols left')
        print('Print a random string containing 0 or 1:\n')
        user = input()
        string += clean(user)
    print('\nFinal data string:')
    print(string + '\n')
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
    return string


def clean(dirty):
    string = [x for x in dirty if x == '1' or x == '0']
    return ''.join(string)


def count(string):
    triad_dict = {key: [0, 0] for key in triad}
    for triple in triad:
        for index, value in enumerate(string):
            if value == triple[0]:
                if (index + 3 <= len(string) - 1) and string[index+1] == triple[1]:
                    if string[index+2] == triple[2]:
                        if string[index+3] == '0':
                            triad_dict[triple][0] += 1
                        elif string[index+3] == '1':
                            triad_dict[triple][1] += 1
    return triad_dict


def generate(user_data):
    random.seed()
    while True:
        try:
            test = ''
            prediction = random.choice(triad)
            print('Print a random string containing 0 or 1:')
            user = input()
            if user == 'enough':
                break
            if int(user):
                test = clean(user)
        except ValueError:
            print()
        else:
            if test:
                for index in range(len(test)-3):
                    triad_entry = user_data[test[index:index+3]]
                    if triad_entry[0] > triad_entry[1]:
                        prediction += '0'
                    else:
                        prediction += '1'
            print('prediction:')
            print(prediction + '\n')
            result(test, prediction)
    print('Game over!')


def result(test, prediction):
    global capital
    correct = 0
    total = len(test) - 3
    for i in range(total):
        if test[i+3] == prediction[i+3]:
            correct += 1
            capital -= 1
        else:
            capital += 1
    percentage = correct / total * 100
    print(f'Computer guessed right {correct} out of {total} symbols ({percentage:.2f} %)')
    print(f'Your capital is now ${capital}\n')


triad = ['000', '001', '010', '011', '100', '101', '110', '111']
capital = 1000

data_string = init()
data = count(data_string)
generate(data)
