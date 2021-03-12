'''
--------------------------------------------------
Name    : Fibonacci String
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/17675
Date    : 11/Feb/2021
--------------------------------------------------
'''
import math


def isPerfectSquare(n):
    x = int(math.sqrt(n))
    if x**2 == n:
        return True
    else:
        return False


def isFibonacciNumber(n):
    if isPerfectSquare(5*n**2+4) or isPerfectSquare(5*n**2-4):
        return True
    else:
        return False


length = int(input())
for i in range(1, length+1):
    if isFibonacciNumber(i):
        print("+", end="")
    else:
        print("-", end="")
