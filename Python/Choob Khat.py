"""
--------------------------------------------------
Name    : Choob Khat
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/contest/80645
Date    : 09/Feb/2021
--------------------------------------------------
"""
import math
m = int(input())
n = int(input())
a = int(input())
b = int(input())
print(math.ceil(min(m, n)/max(a, b)))
