#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Time span """

__author__ = "Lars Schneckenburger"
__credits__ = "Lars Schneckenburger"
__version__ = "1.0.0"
__created__ = "06.03.2021"


'''
    - day()         day in the month
    - month()       month of the year
    - year()        actual year
    
    - add(days)     add days
    - delta(old)    delta of days of two span objects
    - next_month()  increments to beginning of next month
    - next_year()   increments to beginning of next year  
    '''

import datetime

class TimeSpan():
    def __init__(self):
        self.actual =  datetime.datetime.now()

    def __str__(self):
        return self.actual.strftime('%d-%m-%Y') 

    def day(self):
        return int(self.actual.strftime('%d'))

    def month(self):
        return int(self.actual.strftime('%m'))

    def year(self):
        return int(self.actual.strftime('%Y'))

    def add(self, add_days):
        d = datetime.timedelta(days = add_days)
        self.actual += d

    def delta(self, old):
        return (old.actual - self.actual).days

    def next_month(self):
        year = self.actual.strftime('%Y')
        month = self.actual.strftime('%m')
        days_left = (datetime.datetime(int(year), int(month) + 1, 1) - self.actual).days
        self.add(days_left + 1)

    def next_year(self):
        year = self.actual.strftime('%Y')
        days_left = (datetime.datetime(int(year) + 1, 1, 1) - self.actual).days
        self.add(days_left + 1)

    def __format__(self, format_spec):  # formats object for output
        return '{}'.format(self.actual.strftime('%d-%m-%Y'))

# test
if __name__ == "__main__":
    now = TimeSpan()
    print('today:', now)
    print('today: {:02}-{:02}-{:4}'.format(now.day(), now.month(), now.year()))
    print('today is the {}.th day in the month'.format(now.day()))
    print('today is the {}.th day in the year'.format(now.month()))
    print('this is year {}'.format(now.year()))
    
    print('\ncreate a new span object in the future')
    future = TimeSpan() # new Span instance
    future.add(5)   # add 5 days 
    print(future, '> is', now.delta(future), 'days in the future')
    future.next_month()
    print('next month: {} is {} days in the future'.format(future, now.delta(future))) 
    future.next_month()
    print('next month: {} is {} days in the future'.format(future, now.delta(future)))  
    future.next_year()
    print('next year: {} is {} days in the future'.format(future, now.delta(future)))   
