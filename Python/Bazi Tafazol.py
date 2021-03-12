"""
--------------------------------------------------
Name    : Bazi Tafazol
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/technology/87176
Date    : 10/Feb/2021
--------------------------------------------------
"""


def game(number):
    number = list(map(int, str(number)))
    return max(number)-min(number)
