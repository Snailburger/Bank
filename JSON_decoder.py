# -*- coding: utf-8 -*-

""" JSON Decoder """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0"
__created__ = "08.04.2021"

import json
import ast
from SavingAccount import SavingAccount
from YouthAccount import YouthAccount
from Person import Person


class Decoder():

    set_dict_json = {}
    get_dict_json = {}

    def __init__(self, mode):
        if mode == 1:
            self.FILE = 'bankapplication.json'
        elif mode == 2:
            self.FILE = 'test_taxreport.json'

    def record_bank_data(self, data):
        """
        Safe all persons and accounts to file
        """
        counter_key = 1
        for key in data:
            self.set_dict_json[counter_key] = ast.literal_eval(json.dumps(key.__dict__))
            self.set_dict_json[counter_key]["accounts"] = []
            for i in range(len(data[key])):
                x = [data[key][i].__dict__]
                self.set_dict_json[counter_key]["accounts"].append(x)              
            counter_key += 1
        try:
            f = open(self.FILE, 'w')
        except IOError:
            print(("Cannot open file: ") + self.FILE)
        else:
            with f:
                bankaccounts_json = json.dumps(self.set_dict_json, indent = 1)
                f.write(bankaccounts_json)

    def get_bank_data(self):
        """
        Load all persons and accounts to file
        """
        json_load = None
        try:
            f = open(self.FILE, 'r')
        except:
            print(f"File '{self.FILE}' wurde erstellt.")
            f = open(self.FILE, 'w+')
        else:
            with f:
                try:
                    content = f.read()
                    json_load = json.loads(content)
                except Exception as e:
                    print(e)
        if json_load == None:
            dict_bankaccounts = {}
        else:     
            dict_return = {}
            for key in json_load:
                name = json_load[key]["name"]
                age = json_load[key]["age"]
                ahv = json_load[key]["AHV"]
                adress = json_load[key]["adress"]
                dict_return[Person(name, age, ahv, adress)] = []
                if json_load[key]["accounts"]:
                    for i in range(len(json_load[key]["accounts"])):
                        if "age" in json_load[key]["accounts"][i][0].keys():
                            number = json_load[key]["accounts"][i][0]["number"]
                            age = json_load[key]["accounts"][i][0]["age"]
                            balance = json_load[key]["accounts"][i][0]["balance"]
                            print(balance)
                            interest_rate = json_load[key]["accounts"][i][0]["interest_rate"]
                            currency = json_load[key]["accounts"][i][0]["currency"]
                            dict_return[Person(name, age, ahv, adress)].append(YouthAccount(number, age, balance, interest_rate, currency))
                        else:
                            number = json_load[key]["accounts"][i][0]["number"]
                            balance = json_load[key]["accounts"][i][0]["balance"]
                            interest_rate = json_load[key]["accounts"][i][0]["interest_rate"]
                            currency = json_load[key]["accounts"][i][0]["currency"]
                            dict_return[Person(name, age, ahv, adress)].append(SavingAccount(number, balance, interest_rate, currency))
            dict_bankaccounts = dict_return
        return dict_bankaccounts
