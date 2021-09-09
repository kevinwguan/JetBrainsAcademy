# write your code here
import random


def difficulty():
    while True:
        try:
            print("Which level do you want? Enter a number:")
            print(f"1 - {pick_box[1]}")
            print(f"2 - {pick_box[2]}")
            level = int(input())
            if level == 1 or level == 2:
                return level
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


def simple():
    x = random.randint(2, 9)
    op = random.choice(["+", "-", "*"])
    y = random.randint(2, 9)
    print(x, op, y)
    return [x, op, y]


def squared():
    base = random.randint(11, 29)
    print(base)
    return base


def response():
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Incorrect format.")


def check_simple(equation, answer):
    global correct
    result = 0
    if equation[1] == "+":
        result = equation[0] + equation[2]
    elif equation[1] == "-":
        result = equation[0] - equation[2]
    elif equation[1] == "*":
        result = equation[0] * equation[2]
    if result == answer:
        print("Right!")
        correct += 1
    else:
        print("Wrong!")


def check_squared(equation, answer):
    global correct
    if equation ** 2 == answer:
        print("Right!")
        correct += 1
    else:
        print("Wrong!")


def results():
    print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
    save = input()
    yes = ["yes", "YES", "y", "Yes"]
    if save in yes:
        print("What is your name?")
        name = input()
        results_saved(name)
        print('The results are saved in "results.txt".')


def results_saved(name):
    file = open("results.txt", "a")
    file.write(f"{name}: {correct}/5 in level {pick} ({pick_box[pick]}).")
    file.close()


random.seed()
correct = 0
pick_box = {1: "simple operations with numbers 2-9", 2: "integral squares 11-29"}
pick = difficulty()
for i in range(5):
    if pick == 1:
        eq = simple()
        ans = response()
        check_simple(eq, ans)
    elif pick == 2:
        eq = squared()
        ans = response()
        check_squared(eq, ans)
results()
