"""
--------------------------------------------------
Name    : Cube Surface
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/contest/44072
Date    : 11/Feb/2021
--------------------------------------------------
"""
import math


def findMin(volume):
    surfaceAreas = list()
    x = int(math.ceil(volume**(1/3.0)))
    while x >= 1:
        while volume % x:
            x -= 1
        y = int(math.ceil((volume/x)**(1/2.0)))
        while y >= 1:
            while int(volume/x) % y:
                y -= 1
            z = int(volume/(x*y))
            surfaceArea = 2*int(x*y+x*z+y*z)
            surfaceAreas.append(surfaceArea)
            y -= 1
        x -= 1
    return min(surfaceAreas)


print(findMin(int(input())))
