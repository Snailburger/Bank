# -*- coding: utf-8 -*-

""" Youth Account """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0"
__created__ = "19.03.2021"


from BankAccount import BankAccount
from bank_balance_decorator import *
from TimeSpan import TimeSpan

age_limit = 25
withdraw_limit = 2000

class YouthAccount(BankAccount):

    monthly_withdraw = 0

    def __init__(self, number, age, balance = 0, interest_rate = 2, currency = "CHF"):
        super().__init__(number, balance, interest_rate, currency)
        self.age = age
        if age > age_limit:
            raise Exception("You are to old for YouthAccount.")


    def withdraw(self, amount):
        try:
            if self.monthly_withdraw + amount > withdraw_limit:
                raise Exception("Transaction failed. Reached monthly withdraw amount.")
        except Exception as e:
            print(e)
        self.monthly_withdraw += amount
        super().withdraw(amount)


    def get_monthly_withdraw(self):
        return self.monthly_withdraw


# test
if __name__ == "__main__":

    try:
        future = TimeSpan()
        ba2 = YouthAccount("CH00 0000 0000 0000 0000 4446 1", 12)

        # test change interest rate
        print("\n\nTest change interest rate:\n")
        txt = "Interest Rate default[%]:"
        print("{:25}{:10.2f}".format(txt, ba2.get_interest_rate()))  
        ba2.set_interest_rate(3)
        txt = "Interest Rate[%]:"
        print("{:25}{:10.2f}".format(txt, ba2.get_interest_rate()))

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

        # test age limit
        print("\n\nTest age limit:\n")
        age = 30
        print("Person is {} years old".format(age))
        try:
            ba2 = YouthAccount("CH00 0000 0000 0000 0000 5657 1", age)
        except Exception as error:
            print(error)

        # test monthly withdraw limit
        print("\n\nTest monthly withdraw limit:\n")
        ba2.deposit(5000)
        amount = 1500
        future = TimeSpan()
        ba2.withdraw(amount)
        txt = "Date:"
        print("{}".format(ba2.show_span()))
        txt = "Withdraw:"
        print("{:25}{:10.2f}".format(txt, amount))
        txt = "Monthly Withdraw:"
        print("{:25}{:10.2f}".format(txt, ba2.get_monthly_withdraw()))
        txt = "New Withdraw:"
        print("{:25}{:10.2f}".format(txt, amount))
        ba2.withdraw(amount)
        print("\nReset monthly withdraw limit")
        ba2.reset_monthly_withdraw_limit(future)
        future.next_month()
        print("\n{}".format(future))
        print("Reset monthly withdraw limit")
        ba2.reset_monthly_withdraw_limit(future)
        txt = "Monthly Withdraw:"
        print("{:25}{:10.2f}".format(txt, ba2.get_monthly_withdraw()))
    except Exception as error:
        print(error)

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
