# write your code here
import random


def dinner():
    print("Enter the number of friends joining (including you):")
    number = int(input())
    print()
    if number > 0:
        dictionary = create(number)
        bill = pay(dictionary)
        lucky(dictionary, bill)
        print(dictionary)
    else:
        print("No one is joining for the party")


def create(number):
    friend_list = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number):
        friend_list.append(input())
    print()
    return dict.fromkeys(friend_list, 0)


def pay(dictionary):
    print("Enter the total bill value:")
    bill = int(input())
    print()
    split = round(bill / len(dictionary), 2)
    for i in dictionary:
        dictionary[i] = split
    return bill


def lucky(dictionary, bill):
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    decision = input()
    print()
    if decision == "Yes":
        participants = []
        for i in dictionary:
            participants.append(i)
        random.seed()
        chosen = random.choice(participants)
        print(f"{chosen} is the lucky one!")
        print()
        lucky_pay(dictionary, bill, chosen)
    else:
        print("No one is going to be lucky")
        print()


def lucky_pay(dictionary, bill, chosen):
    split = round(bill / (len(dictionary) - 1), 2)
    for i in dictionary:
        if i == chosen:
            dictionary[i] = 0
        else:
            dictionary[i] = split


dinner()
