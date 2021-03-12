'''
--------------------------------------------------
Name    : Hamkari Por Dardesar
Author  : Danial Khorasanizadeh
Link	: https://quera.ir/problemset/contest/3432/
Date    : 05/Feb/2021
--------------------------------------------------
'''
input().split()
mohammadjavadJobs = list(map(int, input().split()))
mostafaJobs = list(map(int, input().split()))
if mostafaJobs == mohammadjavadJobs:
    print("Both")
elif set(mohammadjavadJobs).issubset(mostafaJobs):
    print("Mohammad Javad")
elif set(mostafaJobs).issubset(mohammadjavadJobs):
    print("Mostafa")
else:
    print("None")
