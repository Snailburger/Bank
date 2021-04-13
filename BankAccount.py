# -*- coding: utf-8 -*-

""" Bank account """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0.0"
__created__ = "06.03.2021"


from bank_balance_decorator import *
from TimeSpan import TimeSpan


class BankAccount():

    __span = TimeSpan()

    @set_account
    def __init__(self, number, balance=0, interest_rate=0, currency='CHF'):
        self.number = number
        self.balance = balance
        self.interest_rate = interest_rate
        self.currency = currency

    @safe_balance
    def deposit(self, amount):
        if self.balance + amount > 100000:
            print("Bankbalance can't be over 100'000.")
            return False
        self.balance += amount
        return True

    @safe_balance
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Bankbalance can't be below zero.")
            return False
        self.balance -= amount
        return True

    @safe_balance
    def pay_interest(self, new_span):
        days = BankAccount.__span.delta(new_span)
        interest = 0
        if self.balance > 0:
            interest = self.balance * self.interest_rate * days / 36000
            self.deposit(interest)
            return interest
        return interest
        self.__span.add(days)

    def reset_monthly_withdraw_limit(self, span):
        try:
            if self.__span.month() == span.month():
                 raise Exception("Same Month. Can't reset monthly withdraw limit.")
        except Exception as e:
            print(e)
        self.monthly_withdraw = 0

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def get_currency(self):
        return self.currency

    def get_iban(self):
        return self.number

    def get_balance(self):
        return self.balance

    def get_month(self):
        return self.__span.get

    def show_span(self):
        return self.__span.__format__(self.__span.actual)

    def __repr__(self):
        return '{} : {:10.2f} {}'.format(self.number, self.balance, self.currency)

    def __str__(self):
        return self.number

    def __eq__(self, other):
        return self.number == other


if __name__ == '__main__':
    try:
        ba1 = BankAccount("CH00 0000 0000 0000 0000 0000 1", 50)
        print(ba1)
        ba2 = BankAccount("CH00 0000 0000 0000 0000 1113 1")
        print(ba2)
        ba3 = BankAccount("CH00 0000 0000 0000 0000 0000 2", 70000)
        print(ba3)

        # test normal funktions
        print("\n\nTest normal functions:\n")
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba1.get_balance()))
        txt = "Debosit:"
        amount = 1000
        ba1.deposit(amount)
        print("{:25}{:10.2f}".format(txt, amount))
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba1.get_balance()))
        txt = "Withdraw:"
        amount = 500
        ba1.withdraw(amount)
        print("{:25}{:10.2f}".format(txt, amount))
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba1.get_balance()))

        # test restrictions
        print("\n\nTest restrictions:\n")
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba3.get_balance()))
        txt = "Debosit:"
        amount = 50000
        print("{:25}{:10.2f}".format(txt, amount))
        ba3.deposit(amount)
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba3.get_balance()))
        txt = "Withdraw:"
        amount = 90000
        print("{:25}{:10.2f}".format(txt, amount))
        ba3.withdraw(amount)
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba3.get_balance()))

        # test interest
        future = TimeSpan()
        ba2.deposit(1000)
        ba2.set_interest_rate(1)
        print("\n\nTest pay interest:\n")
        print("{}".format(ba2.show_span()))
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, ba2.get_balance()))
        txt = "Interest Rate:"
        print("{:25}{:10.2f}".format(txt, ba2.get_interest_rate()))
        future.next_year()
        print("\n{}".format(future))
        txt = "Interest:"
        print("{:25}{:10.2f}".format(txt, ba2.pay_interest(future)))
        txt = "New Balance:"
        print("{:25}{:10.2f}".format(txt, ba2.get_balance()))


    except Exception as error:
        print(error)


    print('\ndone')
    print('Author: {}'.format(__author__))
    print("Credits: {}".format(__credits__))
