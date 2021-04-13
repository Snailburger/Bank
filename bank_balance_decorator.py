#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Bank Balance Decorater """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0"
__created__ = "06.03.2021"


import json

# File to safe balances
LOG_FILE = "bank_balance.json"
# Dict to work with balances
dict_bank_account = {}


# Function load specific bank balance
def get_dict():
    global dict_bank_account
    try:
        f = open(LOG_FILE, "r")
    except:
        print(f"File '{LOG_FILE}' wurde erstellt.")
        f = open(LOG_FILE, 'w+')
    else:
        with f:
            try:
                content = f.read()
                dict_bank_account = json.loads(content)
            except Exception as e:
                print(e)


# Funktion to write bank balances to file
def set_dict():
    try:
        f = open(LOG_FILE, "w")
    except IOError:
        print(("Cannot open file: ") + LOG_FILE)
    else:
        with f:
            bank_account_json = json.dumps(dict_bank_account, indent = 4)
            f.write(bank_account_json)


# Decorater to initialize new IBAN or load excisting one
# (set over def __init__)
def set_account(func):
    def wrapper_set_account(*args):
        global dict_bank_account
        # call the function -> do the job
        ret = func(*args)
        # self object of bankaccount
        bank_account = args[0] 
        # load specific bank balance
        get_dict()
        # creat new number in dict_bank_account
        if bank_account.number not in dict_bank_account.keys():
            dict_bank_account[bank_account.number] = bank_account.balance
        # number allready in dict_bank_account
        else:
            print("IBAN exists allready. Amount not charged")
            bank_account.balance = dict_bank_account[bank_account.number]
        # write balances from global bankaccount dict_bank_account to textfile
        set_dict()  # after the function call
        return ret
    return wrapper_set_account


# Decorater to handle balance
# (set over def deposit(self, amount): and def withdraw(self, amount):)
def safe_balance(func):  # decorator with arguments
    def wrapper_safe_balance(*args):
        global dict_bank_account
        # load balances vom textfile to global bankaccount dict_bank_account
        get_dict()
        # self object of bankaccount
        bank_account = args[0]
        # get IBAN
        number = bank_account.number
        # get balance of IBAN
        balance = dict_bank_account[number]
        # give amount back to self object
        bank_account.balance = balance
        # call the function -> do the job
        ret = func(*args)
        # read amount of self object back
        dict_bank_account[number] = bank_account.balance
        # write balances from global bankaccount dict_bank_account to textfile
        set_dict()
        return ret
    return wrapper_safe_balance


# Test
if __name__ == "__main__":
    class Account():
        @set_account
        def __init__(self, number, balance = 0):
            self.number = number
            self.balance = balance

        @safe_balance
        def deposit(self, amount):
            if self.balance + amount <= 100000:
                self.balance += amount

        @safe_balance
        def withdraw(self, amount):
            if self.balance - amount >= 0:
                self.balance -= amount

        def get_saldo(self):
            return self.balance

        def __repr__(self):
            return("{} : {:10.2f} {}".format(
                self.number, self.balance, self.currency))

    try:
        # if an IBAN allready excists, the amount given to the init is ignored
        a1 = Account("CH00 0000 0000 3454 0000 0", 50)
        a2 = Account("CH00 0000 0000 2345 0000 0", 100000)
        a3 = Account("CH00 0000 0000 2365 0000 0")
        print()
        print("Safed Balances")
        print(a1.get_saldo())
        print(a2.get_saldo())
        print(a3.get_saldo())
        a1.deposit(100)
        a1.withdraw(50)
        a2.withdraw(5)
        a3.deposit(1000000)
        a3.withdraw(50000)
        print()
        print("New balances")
        print(a1.get_saldo())
        print(a2.get_saldo())
        print(a3.get_saldo())

    except Exception as error:
        print(error)

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
