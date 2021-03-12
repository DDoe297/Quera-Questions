'''
--------------------------------------------------
Name    : Better Life
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/10325
Date    : 11/Feb/2021
--------------------------------------------------
'''
row, column = map(int, input().split())
endPrint = list()
if(column <= 10):
    endPrint.append("Right")
    endPrint.append(str(11-row))
    endPrint.append(str(column))
else:
    endPrint.append("Left")
    endPrint.append(str(11-row))
    endPrint.append(str(21-column))
print(*endPrint)
