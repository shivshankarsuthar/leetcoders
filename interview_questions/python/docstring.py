#!/usr/bin/env
def foo(a,b):
    '''This is a function to print Foo\nThis is second line'''
    print("Foo")

print(foo.__doc__)
print(__name__)
print(__file__)
# help(foo)