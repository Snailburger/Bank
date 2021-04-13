# -*- coding: utf-8 -*-

""" Bank Application Interface """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1."
__created__ = "21.03.2021"


from BankApplication import BankApplication

# Programm
choose_option_1 = {"1": "Creat Person",
                      "2": "Log in",
                      "3": "Leave"}
options_1 = ["1", "2", "3"]

choose_option_2 = {"1": "Add account",
                      "2": "Manage account",
                      "3": "Leave"}
options_2 = ["1", "2", "3"]

choose_option_3 = {"1": "Youth account",
                      "2": "Saving account",
                      "3": "Leave"}
options_3 = ["1", "2", "3"]

choose_option_4 = {"1": "Get Saldo",
                      "2": "Deposit",
                      "3": "Withdraw",
                      "4": "Transfere",
                      "5": "Leave"}
options_4 = ["1", "2", "3", "4", "5"]

app = BankApplication()

app.load_bank_application()

while True:
    print("\n\n-Bank application-\n")
    while True:
        for key, value in choose_option_1.items():
            print(key, ': ', value)
        option = input("->")
        if option not in options_1:
            print(f"Invalid input. Choose a number between 1 and {len(options_1)}!")
        else:
            option = int(option)
            break

    if option == 1:
        print("\n-Create new Person-")
        name = input("Name: ")
        age = int(input("Age: "))
        ahv = input("AHV: ")
        adress = input("Adress: ")
        if app.creat_person(name, age, ahv, adress):
            print("\nNew person created\n")
        else:
            print("Failed.")

    elif option == 2:
        print("\n-Log in-")
        ahv = input("Input AHV: ")
        if app.set_person(ahv):
            print("\nYou logged in.\n")
            
            while True:
                if not app.dict_bankaccounts[app.person]:
                    print("You have no account. Creat one.")
                    option = 1
                else:
                    while True:
                        for key, value in choose_option_2.items():
                            print(key, ': ', value)
                        option = input("->")
                        if option not in options_2:
                            print(f"Invalid input. Choose a number between 1 and {len(options_2)}!")
                        else:
                            option = int(option)
                            break

                if option == 1:
                    print("\n-Add Account-")
                    while True:
                        for key, value in choose_option_3.items():
                            print(key, ': ', value)
                        option = input("->")
                        if option not in options_3:
                            print(f"Invalid input. Choose a number between 1 and {len(options_3)}!")
                        else:
                            option = int(option)
                            break
                    if option == 1:
                        acc = "YouthAccount"
                        if app.add_account(ahv, acc):
                            print("Account added.\n")
                    
                    elif option == 2:
                        acc = "SavingAccount"
                        if app.add_account(ahv, acc):
                            print("Account added.\n")
                    else:
                        break

                elif option == 2:
                    while True:
                        print("\nYour Accounts:")
                        for i in range(len(app.dict_bankaccounts[app.person])):
                            print(f"{i + 1} -> {app.dict_bankaccounts[app.person][i]}")
                        print(f"{i + 2} -> Leave")
                        x = int(input("->")) - 1
                        if  x < (i + 1):
                            app.set_account(app.dict_bankaccounts[app.person][x].__str__())
                            while True:
                                print("\n-Manage account-")
                                while True:
                                    for key, value in choose_option_4.items():
                                        print(key, ': ', value)
                                    option = input("->")
                                    if option not in options_4:
                                        print(f"Invalid input. Choose a number between 1 and {len(options_4)}!")
                                    else:
                                        option = int(option)
                                        break

                                if option == 1:
                                    print(f"\nSaldo: {app.account.get_balance()}")
                                
                                elif option == 2:
                                    amount = int(input("Amount: "))
                                    app.account.deposit(amount)
                                
                                elif option == 3:
                                    amount = int(input("Amount: "))
                                    app.account.withdraw(amount)
                                
                                elif option == 4:
                                    iban = input("IBAN: ")
                                    amount = int(input("Amount: "))
                                    iban_set = app.account.number
                                    app.transfere(iban_set, iban, amount)
                                else:
                                    break
                        else:
                            break
                else:
                    break
    else:
        break


app.safe_bank_application()

# test
if __name__ == "__main__":

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
