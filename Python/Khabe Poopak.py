"""
--------------------------------------------------
Name    : Khabe Poopak
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/contest/15124 
Date    : 10/Feb/2021
--------------------------------------------------
"""
a, b, x = map(int, input().split())
counter = 0
for i in range(1, a+1):
    if(a % i != 0):
        continue
    else:
        for j in range(1, b+1):
            if(b % j != 0):
                continue
            elif (i+j <= x):
                counter += 1
print(counter)
