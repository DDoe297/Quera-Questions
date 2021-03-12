'''
--------------------------------------------------
Name    : Test Binaei
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/2659
Date    : 12/Feb/2021
--------------------------------------------------
'''
input()
firstString = input()
secondString = input()
count = 0
for i in range(len(firstString)):
    if firstString[i] != secondString[i]:
        count += 1
print(count)
