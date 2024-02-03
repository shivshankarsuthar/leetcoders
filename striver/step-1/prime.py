from math import *
from collections import *
from sys import *
from os import *

n = int(input())
foundAPrimeNumber = False
if n == 1:
    print('NO')
    foundAPrimeNumber = True
for i in range(2,int(n**0.5)+1):
    if(n % i == 0):
        foundAPrimeNumber = True
        print('NO')
        break

if not foundAPrimeNumber:
    print('YES')

