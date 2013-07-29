'''
Aaron Gotlieb
'''

from board import *
from piece import *

print("Welcome to (Z)Checkers!")
print("Ready Player 1")


j = [[1 for x in range(8)] for x in range(8)]
b = board(j)

for x in range (8):
	print(b.board[x])

xloc = 1
yloc = 2
isKing = False
color = 3
player = 1

p = piece(xloc, yloc, isKing, color, player)
pie = p.getPiece()
p.printPiece()
b.addPiece(b, p.x, p.y, p.color)

for x in range (8):
	print(b.board[x])




