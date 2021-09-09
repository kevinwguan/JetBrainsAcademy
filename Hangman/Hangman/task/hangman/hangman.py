# Write your code here
import random
import string

library = ['python', 'java', 'kotlin', 'javascript']
alphabet = list(string.ascii_lowercase)
choice = random.choice(library)
guess_history = []
valid_letters = set(choice)
attempts = 8


def menu():
    print('H A N G M A N')
    while True:
        user = input('Type "play" to play the game, "exit" to quit: ')
        if user == 'play':
            game()
        elif user == 'exit':
            break


def game():
    global attempts
    hidden = '-' * len(choice)
    while attempts > 0:
        print('\n' + hidden)
        guess = input('Input a letter: ')
        if guess in guess_history:
            print("You've already guessed this letter")
            continue
        elif len(guess) != 1:
            print('You should input a single letter')
            continue
        elif guess not in alphabet:
            print('Please enter a lowercase English letter')
            continue
        else:
            hidden = check(guess, hidden)
            guess_history.append(guess)
        if hidden == choice:
            print()
            print(hidden)
            print('You guessed the word!')
            print('You survived!')
            break
    else:
        print('You lost!')


def check(letter, hidden):
    global attempts
    if letter in valid_letters:
        hidden_list = list(hidden)
        uncover = choice.count(letter)
        uncover_start_index = 0
        uncover_index = []
        while len(uncover_index) != uncover:
            x = choice.index(letter, uncover_start_index)
            uncover_index.append(x)
            uncover_start_index = x + 1
        for i in uncover_index:
            hidden_list[i] = choice[i]
        return ''.join(hidden_list)
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
        return hidden


menu()
