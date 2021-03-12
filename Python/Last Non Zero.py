'''
--------------------------------------------------
Name    : Last non zero digit of n!
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/3411/
Date    : 11/Feb/2021
--------------------------------------------------
'''


def lastNonZeroDigit(n):
    lastDigit = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]
    if (n < 10):
        return lastDigit[n]
    if (((n//10) % 10) % 2 == 0):
        return (6*lastNonZeroDigit(n//5)*lastDigit[n % 10]) % 10
    else:
        return (4*lastNonZeroDigit(n//5)*lastDigit[n % 10]) % 10
    return 0


print(lastNonZeroDigit(int(input())))
