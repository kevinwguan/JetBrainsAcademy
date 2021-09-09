# Write your code here
import random
import sqlite3


def main_menu():
    client = Database()
    # client.cur.execute("delete from card")
    count = 1
    while True:
        print("1. Create an Account")
        print("2. Log into account")
        print("0. Exit")
        user = int(input())
        print()
        if user == 1:
            customer = Account()
            client.write(count, customer.credit_card, customer.pin)
            count += 1
        elif user == 2:
            session = login(client)
            if session:
                user = sub_menu(client, session)
        if user == 0:
            print("Bye!")
            break


def sub_menu(client, session):
    while True:
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        user = int(input())
        print()
        if user == 1:
            balance(client, session)
        elif user == 2:
            income(client, session)
        elif user == 3:
            transfer(client, session)
        elif user == 4:
            close(client, session)
        elif user == 5:
            print("You have successfully logged out!")
            print()
            return user
        if user == 0:
            return user


def login(client):
    print("Enter your card number:")
    number = input()
    print("Enter your PIN:")
    pin = input()
    print()
    auth = client.handshake(number, pin)
    if auth:
        print("You have successfully logged in!")
        print()
        return {1: number, 2: pin}
    else:
        print("Wrong card number or PIN!")
        print()
        return 0


def balance(client, session):
    print(client.handshake(session[1], session[2])[3])
    print()


def income(client, session):
    print("Enter income:")
    amount = int(input())
    row = client.handshake(session[1], session[2])
    amount += row[3]
    client.modify(row[0], row[1], row[2], amount)
    print("Income was added!")
    print()


def transfer(client, session):
    print("Transfer")
    print("Enter card number:")
    number = input()
    if verify(number):
        row1 = client.check(number)
        if row1:
            print("Enter how much money you want to transfer")
            funds = int(input())
            current = client.handshake(session[1], session[2])[3]
            if funds < current:
                current -= funds
                row2 = client.handshake(session[1], session[2])
                client.modify(row1[0], row1[1], row1[2], funds)
                client.modify(row2[0], row2[1], row2[2], current)
                print("Success!")
                print()
            else:
                print("Not enough money!")
                print()
        else:
            print("Such a card does not exist.")
            print()
    else:
        print("Probably you made a mistake in the card number. Please try again!")
        print()


def verify(number):
    array = list(number)
    result = 0
    for i, j in enumerate(array):
        array[i] = int(j)
        if i % 2 == 0:
            array[i] *= 2
        if array[i] > 9:
            array[i] -= 9
        result += array[i]
    if result % 10 == 0:
        return 1
    else:
        return 0


def close(client, session):
    client.remove(session[1], session[2])
    print("The account has been closed!")
    print()


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("card.s3db")
        self.cur = self.conn.cursor()
        # self.cur.execute("create table card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
        # self.conn.commit()

    def read(self):
        self.cur.execute(f"select * from card")
        return self.cur.fetchall()

    def handshake(self, number, pin):
        row = self.read()
        for i, j in enumerate(row):
            if j[1] == number and j[2] == pin:
                return row[i]
        else:
            return 0

    def check(self, number):
        row = self.read()
        for i, j in enumerate(row):
            if j[1] == number:
                return row[i]
        else:
            return 0

    def write(self, count, number, pin):
        self.cur.execute(f"insert into card (id, number, pin) values ({count}, {number}, {pin})")
        self.conn.commit()

    def modify(self, count, number, pin, amount):
        self.cur.execute(f"delete from card where number = {number} and pin = {pin}")
        self.cur.execute(f"insert into card values ({count}, {number}, {pin}, {amount})")
        self.conn.commit()

    def remove(self, number, pin):
        self.cur.execute(f"delete from card where number = {number} and pin = {pin}")
        self.conn.commit()


class Account:

    def __init__(self):
        self.bank_identification = "400000"
        self.number = ""
        self.checksum = ""
        self.credit_card = ""
        self.pin = ""
        self.balance = 0
        self.generate()

    def generate(self):
        random.seed()
        self.number = f"{random.randint(000000000, 999999999):09}"
        self.pin = f"{random.randint(0000, 9999):04}"
        self.luhn()
        self.process()

    def luhn(self):
        array = list(self.number)
        result = 8
        for i, j in enumerate(array):
            array[i] = int(j)
            if i % 2 == 0:
                array[i] *= 2
            if array[i] > 9:
                array[i] -= 9
            result += array[i]
        self.checksum = "0" if result % 10 == 0 else str(10 - result % 10)

    def process(self):
        self.credit_card = self.bank_identification + self.number + self.checksum
        print("Your card has been created")
        print("Your card number:")
        print(self.credit_card)
        print("Your card PIN:")
        print(self.pin)
        print()


main_menu()
