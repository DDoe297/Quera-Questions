'''
--------------------------------------------------
Name    : Reverse String
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/3408
Date    : 12/Feb/2021
--------------------------------------------------
'''
input()
string = list(input().split())
for i in range(len(string)-1, -1, -1):
    print(string[i], end=" ")
