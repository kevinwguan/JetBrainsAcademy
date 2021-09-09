import argparse
import math

from collections import namedtuple

Financials = namedtuple('Financials', ['type', 'payment', 'principal', 'periods', 'interest'])


def main_menu():
    user = init()
    user = convert_to_number(user)
    if valid(user):
        if user.type == 'annuity':
            annuity(user)
        elif user.type == 'diff':
            diff(user)


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--payment')
    parser.add_argument('--principal')
    parser.add_argument('--periods')
    parser.add_argument('--interest')
    args = parser.parse_args()
    return Financials(args.type, args.payment, args.principal, args.periods, args.interest)


def valid(user):
    if user.type not in ['annuity', 'diff']:
        print('Incorrect parameters')
        return False
    elif user.type == 'diff' and user.payment:
        print('Incorrect parameters')
        return False
    elif not user.interest:
        print('Incorrect parameters')
        return False
    elif user.count(None) > 1:
        print('Incorrect parameters')
        return False
    for i in user[1:]:
        if i:
            if int(i) < 0:
                print('Incorrect parameters')
                return False
    return True


def convert_to_number(user):
    converted = [user[0]]
    for i in user[1:]:
        try:
            converted.append(float(i))
        except TypeError:
            converted.append(None)
    return Financials(converted[0], converted[1], converted[2], converted[3], converted[4])


def prep(user):
    for i in user:
        if not i:
            return user.index(i)


def diff(user):
    overpayment = 0
    interest = user.interest / (12 * 100)
    for i in range(1, int(user.periods) + 1):
        first = user.principal - user.principal * (i - 1) / user.periods
        payment = user.principal / user.periods + interest * first
        payment = math.ceil(payment)
        overpayment += payment - user.principal / user.periods
        print(f'Month {i}: payment is {payment}')
    print()
    print(f'Overpayment = {int(overpayment)}')


def annuity(user):
    def option_a():
        interest = user.interest / (12 * 100)
        numerator = interest * (1 + interest) ** user.periods
        denominator = (1 + interest) ** user.periods - 1
        payment = user.principal * numerator / denominator
        payment = math.ceil(payment)
        overpayment = payment * user.periods - user.principal
        overpayment = int(overpayment)
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {overpayment}')

    def option_p():
        interest = user.interest / (12 * 100)
        numerator = interest * (1 + interest) ** user.periods
        denominator = (1 + interest) ** user.periods - 1
        principal = user.payment * denominator / numerator
        principal = math.floor(principal)
        overpayment = user.payment * user.periods - principal
        overpayment = int(overpayment)
        print(f'Your loan principal = {principal}!')
        print(f'Overpayment = {overpayment}')

    def option_n():
        interest = user.interest / (12 * 100)
        months = math.log(user.payment / (user.payment - interest * user.principal), 1 + interest)
        months = math.ceil(months)
        years = months // 12
        remaining_months = months % 12
        start_string = 'It will take' + ' '
        end_string = 'to repay this loan!'
        if years > 1:
            start_string += f'{years} years' + ' '
        elif years == 1:
            start_string += f'{years} year' + ' '
        if years and months:
            start_string += 'and' + ' '
        if remaining_months > 1:
            start_string += f'{remaining_months} months' + ' '
        elif remaining_months == 1:
            start_string += f'{remaining_months} month' + ' '
        overpayment = user.payment * months - user.principal
        overpayment = int(overpayment)
        print(start_string + end_string)
        print(f'Overpayment = {overpayment}')

    index = prep(user)
    if index == 1:
        option_a()
    elif index == 2:
        option_p()
    elif index == 3:
        option_n()


# write your code here
main_menu()
