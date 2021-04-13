# -*- coding: utf-8 -*-

""" Tax reporting """

__author__ = 'Lars Schneckenburger'
__credits__ = 'Lars Schneckenburger'
__version__ = '2.0.0'
__created__ = '30.03.2021'


from CurrencyConverter import CurrencyConverter
from JSON_decoder import Decoder
from TimeSpan import TimeSpan


class TaxReport():

    __span = TimeSpan()
    currency = CurrencyConverter()

    def __init__(self):
        pass

    def generate(self, dict_bankaccounts):
        fiscal_year = TaxReport.__span.year()
        TaxReport.__span.next_year()
        current_year = TaxReport.__span.year()
        print("\n\nTax report {} for fiscal year {}:\n".format(current_year, fiscal_year))
        for key in dict_bankaccounts:
            print(key)
            for i in range(len(dict_bankaccounts[key])):
                print(dict_bankaccounts[key][i].__repr__())
                if dict_bankaccounts[key][i].currency.lower() != "chf":
                    cur = dict_bankaccounts[key][i].currency
                    amount = dict_bankaccounts[key][i].balance
                    print("{:39.2f} CHF".format(self.currency.convert_amount(cur, "chf", amount)))
            print()


if __name__ == '__main__':

    data = Decoder(2).get_bank_data()
    TaxReport().generate(data)

    print('\ndone')
    print('Author: {}'.format(__author__))
    print("Credits: {}".format(__credits__))
