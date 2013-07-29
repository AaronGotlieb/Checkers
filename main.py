'''
Aaron Gotlieb
'''

from board import *
from piece import *

print("Welcome to (Z)Checkers!")
print("Ready Player 1")
b = board()
j = b.getBoard()

loc = 1
isKing = False
color = 'Red'
player = 1

p = piece(loc, isKing, color, player)
pie = p.getPiece()
p.printPiece()

print("peice:")
print(pie.loc)

for x in range (8):
	print(j[x])



