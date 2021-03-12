'''
--------------------------------------------------
Name    : BMI Calculate
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/3404
Date    : 12/Feb/2021
--------------------------------------------------
'''


def cut(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


weight = int(input())
height = float(input())
BMI = weight/height**2
print("%.2f" % BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")
