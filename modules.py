import sys

def sys_mod():
    v = sys.version_info
    print("Python version: {}.{}.{}".format(*v))
    print("-----------------------------------")

sys_mod()

import os

def os_mod():
    v = os.name
    w = os.getcwd()
    print(f'Operating system: {v}')
    print(f'Current Working Directory: {w}')
    print("-----------------------------------")

os_mod()

# imports module and assign to an object
import datetime as date

def date_time():
    now = date.datetime.now()
    print(f'Now: {now}')
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')
    print(f'Date: {now.day}/{now.month}/{now.year}')

date_time()