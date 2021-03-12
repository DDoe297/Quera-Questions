'''
--------------------------------------------------
Name    : Chess
Author  : Danial Khorasanizadeh
Link	: quera.ir/problemset/contest/2636
Date    : 11/Feb/2021
--------------------------------------------------
'''
correctPieces = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))
print(*[correctPieces[piece]-pieces[piece] for piece in range(6)])
