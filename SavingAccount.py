# -*- coding: utf-8 -*-

""" Saving Account """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0.0"
__created__ = "18.03.2021"


from BankAccount import BankAccount
from bank_balance_decorator import *
from TimeSpan import TimeSpan

additional_charge = 2

class SavingAccount(BankAccount):

    def __init__(self, number, balance = 0, interest_rate = 0.1, currency = "CHF"):
        super().__init__(number, balance, interest_rate, currency)

    @safe_balance
    def withdraw(self, amount):
        # additional 2% charge for withdraw below zero
        charge = 0
        if self.balance - amount < 0:
            if self.balance > 0:
                charge = abs(self.balance - amount) * (additional_charge / 100)
            else:
                charge = amount * (additional_charge / 100)
            self.balance -= amount + charge
        else:
            self.balance -= amount
        return charge


# test
if __name__ == "__main__":

    try:
        ba1 = SavingAccount("CH00 0000 0000 0000 0000 9463 1", interest_rate = 0.2)
        ba2 = SavingAccount("CH00 0000 0000 0000 0000 8713 1", interest_rate = 0.2)

        # test additional charge below zero
        amount = 1000
        print("\n\nTest additional charge below zero\n")
        txt = "Balance:"
        print("{:15}{:15.2f}".format(txt, ba1.get_balance()))
        txt = "Withdraw:"
        print("{:15}{:15.2f}".format(txt, amount))
        txt = "Charge:"
        print("{:15}{:15.2f}".format(txt, ba1.withdraw(amount)))
        txt = "New Balance:"
        print("{:15}{:15.2f}".format(txt, ba1.get_balance()))

        # test interest
        future = TimeSpan()
        ba2.deposit(1000)
        ba2.set_interest_rate(1)
        print("\n\nTest pay interest:\n")
        print("{}".format(ba2.show_span()))
        txt = "Balance:"
        print("{:15}{:15.2f}".format(txt, ba2.get_balance()))
        txt = "Interest Rate:"
        print("{:15}{:15.2f}".format(txt, ba2.get_interest_rate()))  
        future.next_year()
        print("\n{}".format(future))
        txt = "Interest:"
        print("{:15}{:15.2f}".format(txt, ba2.pay_interest(future)))
        txt = "New Balance:"
        print("{:15}{:15.2f}".format(txt, ba2.get_balance()))

    except Exception as error:
        print(error)

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
