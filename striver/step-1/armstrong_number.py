from os import *
from sys import *
from collections import *
from math import *

number = int(input())
copied_number = number
digits = []
while copied_number != 0:
    digits.append(copied_number % 10)
    copied_number //= 10
total = 0
for digit in digits:
    total += digit ** len(digits)

if total == number:
    print('true')
else:
    print('false')