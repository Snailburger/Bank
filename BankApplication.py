# -*- coding: utf-8 -*-

""" Bank Application """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0"
__created__ = "21.03.2021"


from SavingAccount import SavingAccount
from YouthAccount import YouthAccount
from Person import Person
from TaxReport import TaxReport
from JSON_decoder import Decoder
import random


FILE_BANKACCOUNTS = "bankapplication.json"


class BankApplication():

    __tax = TaxReport()
    __decoder = Decoder(1)
    person = None
    account = None

    def __init__(self):
        self.dict_bankaccounts = self.__decoder.get_bank_data()

    def creat_iban(self):
        """
        Returns
        -------
        iban : string
            New IBAN for new Account.
        """
        check = False
        while check == False:
            check = True
            iban = "CH34 2345 3"
            for i in range(15):
                if i in [3, 8, 13]:
                    iban += " "
                else:
                    n = int(random.uniform(1, 10))
                    iban += f"{n}"
            for key in self.dict_bankaccounts:
                for i in range(len(self.dict_bankaccounts[key])):
                    if iban == self.dict_bankaccounts[key][i].__str__():
                        check = False
            if check == True:
                return iban

    def creat_person(self, name, age, AHV, adress):
        """
        Parameters
        ----------
        name : string
            Name Person.
        age : int
            Age Person.
        AHV : string
            AHV Number.
        adress : string
            Adress Person.

        Returns
        -------
        check : boolean
            True if Person created.
        """
        check = True
        if self.dict_bankaccounts:
            for key in self.dict_bankaccounts:
                if Person(name, age, AHV, adress) == key:
                    check = False
        if check != False:
            self.dict_bankaccounts[Person(name, age, AHV, adress)] = []
        return check

    def set_person(self, ahv):
        """
        Parameters
        ----------
        ahv : string
            AHV to indentifie person.

        Returns
        -------
        check : Boolean
            True if Person found.
        """
        check = False
        for key in self.dict_bankaccounts:
            if hash(ahv) == key.__hash__():
                check = True
                self.person = key
        return check

    def current_person(self):
        """
        Returns
        -------
        dict person
            If a person is activated.
        False
            If no person is activated
        """
        if self.person:
            return self.person.__dict__
        else:
            return False

    def set_account(self, iban):
        """
        Parameters
        ----------
        iban : string
            IBAN to identify account.

        Returns
        -------
        check : bool
            True if account found.
        """
        check = False
        for key in self.dict_bankaccounts:
            for i in range(len(self.dict_bankaccounts[key])):
                if iban == self.dict_bankaccounts[key][i].__str__():
                    self.account = self.dict_bankaccounts[key][i]
                    check = True
        return check

    def current_account(self):
        """
        Returns
        -------
        dict account
            If a account is activated.
        False
            If no account is activated
        """
        if self.account:
            return self.account.__dict__
        else:
            return False

    def add_account(self, ahv, account):
        """
        Add account to current person.
        Parameters
        ----------
        ahv : string
            From person which account shoud be added.
        account : String
            What type of account shoud be added to person.

        Returns
        -------
        check : Boolean
            True if Account added.
        """
        self.set_person(ahv)
        if self.current_person():
            iban = self.creat_iban()
            age = self.person.get_age()
            check = False
            if account == "YouthAccount":
                self.dict_bankaccounts[self.person].append(YouthAccount(iban, age))
                if age < 26:
                    check = True
                    print(f"Your new IBAN: {iban}")
            elif account == "SavingAccount":
                self.dict_bankaccounts[self.person].append(SavingAccount(iban))
                print(f"Your new IBAN: {iban}")
                check = True
            return check
        else:
            return False

    def delet_account(self, ahv, iban):
        """
        Parameters
        ----------
        ahv : string
            AHV of person.
        iban : string
            DESCRIPTION.

        Returns
        -------
        check : Boolean
            True if account deleted.
        """
        check = False
        self.set_person(ahv)
        for i in range(len(self.dict_bankaccounts[self.person])):
            if iban == self.dict_bankaccounts[self.person][i].number:
                del self.dict_bankaccounts[self.person][i]
                check = True
        return check

    def transfere(self, iban_withdraw, iban_deposit, amount):
        """
        Transfer amount from current account to other account.

        Parameters
        ----------
        iban_withdraw : String
            Account to withdraw amount.
        iban_deposit : String
            Account to deposit amount.
        amount : int
            Amount to transfer.

        Returns
        -------
        check_transfer : boolean
            Returns True if transfer completed.

        """
        check_1 = False
        check_2 = False
        check_transfer = False
        for key_1 in self.dict_bankaccounts:
            for i in range(len(self.dict_bankaccounts[key_1])):
                if iban_withdraw == self.dict_bankaccounts[key_1][i].number:
                    check_1 = True
                    break
            else:
                continue
            break
        for key_2 in self.dict_bankaccounts:
            for j in range(len(self.dict_bankaccounts[key_2])):
                if iban_deposit == self.dict_bankaccounts[key_2][j].number:
                    check_2 = True
                    break
            else:
                continue
            break
        if check_1 == True and check_2 == True:
            self.dict_bankaccounts[key_1][i].withdraw(amount)
            self.dict_bankaccounts[key_2][j].deposit(amount)
            check_transfer = True
            return check_transfer
        else:
            return check_transfer

    def tax_report(self):
        """
        Returns
        -------
        Prints Tax Report.

        """
        self.__tax.generate(self.dict_bankaccounts)

    def record_data(self):
        """
        Record Bankapplication Data.

        """
        self.__decoder.record_bank_data(self.dict_bankaccounts)
        print("Data recorded.")


# test
if __name__ == "__main__":

    app = BankApplication()

    try:
        # test load file
        print("\n\n-Load Persons/Accounts from File-\n")
        print(app.dict_bankaccounts)

        # test creat person
        print("\n\n-Create new Person-\n")
        txt = "Name:"
        name = "Hans Muster"
        print("{:25}{:25}".format(txt, name))
        txt = "Age:"
        age = 22
        print("{:25}{:0}".format(txt, age))
        txt = "AHV:"
        ahv = "23.345.67"
        print("{:25}{:25}".format(txt, ahv))
        txt = "Adress:"
        adress = "Winterthur"
        print("{:25}{:25}".format(txt, adress))
        if app.creat_person(name, age, ahv, adress):
            print("\nNew person created\n")
        else:
            print("\nPerson exists allready\n")

        # test set person
        print("\n\n-Set Person-\n")
        txt = "ID-number = AHV"
        ahv = "23.345.67"
        print("{:25}{:25}".format(txt, ahv))
        app.set_person(ahv)
        print(app.person)

        # test get current person
        print("\n\n-Current Person-\n")
        print(app.current_person())

        # get
        print("\n\n-Accounts from person-")
        print(f"{app.dict_bankaccounts[app.person]}")

        # test add account
        print("\n\n-Add Account-\n")
        txt = "Account:"
        acc = "YouthAccount"
        print("{:25}{:25}".format(txt, acc))
        if app.add_account(ahv, acc):
            print("Account added.")

        # test set account
        print("\n\n-Set Account-\n")
        txt = "ID-number = IBAN"
        iban = app.dict_bankaccounts[app.person][0].number
        print("{:25}{:25}".format(txt, iban))
        app.set_account(iban)
        print(app.account)

        # test get current account
        print("\n\n-Current Account-\n")
        print(app.current_account())

        # test functions
        print("\n\n-Withdraw/Deposit-\n")
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, app.account.get_balance()))
        txt = "Debosit:"
        amount = 1000
        app.account.deposit(amount)
        print("{:25}{:10.2f}".format(txt, amount))
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, app.account.get_balance()))
        txt = "Withdraw:"
        amount = 100
        app.account.withdraw(amount)
        print("{:25}{:10.2f}".format(txt, amount))
        txt = "Balance:"
        print("{:25}{:10.2f}".format(txt, app.account.get_balance()))

        # test transfere
        print("\n\n-Transfere-\n")
        name = "Julius Caesar"
        age = 1250
        ahv_2 = "56.436.23"
        adress = "Rom"
        app.creat_person(name, age, ahv_2, adress)
        acc = "SavingAccount"
        app.add_account(ahv_2, acc)
        app.set_person(ahv_2)
        iban_2 = app.dict_bankaccounts[app.person][0].get_iban()
        print("Account 1:")
        print(app.current_account())
        print("Account 2:")
        app.set_account(iban_2)
        print(app.current_account())
        amount = 500
        if app.transfere(iban, iban_2, amount):
            print("\nTransfer of {} completed\n".format(amount))
        print("Account 1:")
        app.set_account(iban)
        print(app.current_account())
        print("Account 2:")
        app.set_account(iban_2)
        print(app.current_account())

        # tax reporting
        print("\n")
        app.creat_person("Max Müller", 35, "123.3456.123", "Winterthur")
        app.add_account("123.3456.123", "SavingAccount")
        app.set_account(app.dict_bankaccounts["123.3456.123"][0])
        app.account.deposit(1200)

        app.creat_person("Erik Zimmer", 60, "438.2746.402", "Zürich")
        app.add_account("438.2746.402", "SavingAccount")
        app.set_account(app.dict_bankaccounts["438.2746.402"][0])
        app.account.deposit(55340)
        app.add_account("438.2746.402", "SavingAccount")
        app.set_account(app.dict_bankaccounts["438.2746.402"][1])
        app.account.withdraw(20000)

        app.tax_report()

        # safe global dict to file to file
        print("\n\n-Safe Persons/Accounts to File-\n")
        app.record_data()

    except Exception as error:
        print(error)

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
