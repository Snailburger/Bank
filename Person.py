# -*- coding: utf-8 -*-

""" Person """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0.0"
__created__ = "25.03.2021"


import json

class Person():
    def __init__(self, name, age, AHV, adress):
        self.name = name
        self.age = age
        self.AHV = AHV
        self. adress = adress

    def __hash__(self):
        return hash(self.AHV)

    def __eq__(self, AHV):
        return self.AHV == AHV

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


if __name__ == "__main__":

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
