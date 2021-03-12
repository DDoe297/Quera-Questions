"""
--------------------------------------------------
Name    : Bazi Ba Aadad Dar Barareh
Author  : Danial Khorasanizadeh
Link    : https://quera.ir/problemset/contest/10168
Date    : 10/Feb/2021
Note    : Not complete
--------------------------------------------------
"""
import math


def findDivisors(n):
    i = 1
    divisors = list()
    while (i * i < n):
        if (n % i == 0):
            divisors.append(i)
        i += 1
    for i in range(int(math.sqrt(n)), 0, -1):
        if (n % i == 0):
            divisors.append(n // i)
    return divisors


def findSteps(shirfarhadNumber, kianooshNumber):
    counter = 0
    while shirfarhadNumber < kianooshNumber:
        divisors = findDivisors(shirfarhadNumber)
        n = -2
        while(shirfarhadNumber+divisors[n] > kianooshNumber):
            n -= 1
        if(divisors[n] == 1):
            return -1
        else:
            shirfarhadNumber += divisors[n]
            counter += 1
            print(shirfarhadNumber)
    return counter


shirfarhadNumber, kianooshNumber = map(int, input().split())
print(findSteps(shirfarhadNumber, kianooshNumber))
