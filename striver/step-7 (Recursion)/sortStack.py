from os import *
from sys import *
from collections import *
from math import *

# S is a list of integers
def sortIt(s,key):
    if len(s) == 0 or s[-1] < key:
        s.append(key)
        return 
    
    top = s[-1]
    s.pop()
    sortIt(s,key)
    s.append(top)

def sortStack(s):
    # Write your code here.
    if len(s) == 0:
        return
    
    top = s[-1]
    s.pop()
    sortStack(s)
    sortIt(s,top)
    return s

print(sortStack([1,0,0,2]))