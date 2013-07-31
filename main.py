'''
Aaron Gotlieb
'''

from board import *
#from piece import *

print("Welcome to (zork)Checkers!")
print("Ready Player 1")

j = 'nothing'
b = board()
print("flag1")
print(b)
#b.printBoard(b)

print("flag2")
b.setUp(b.board)

b.printBoard(b.board)

b.getColor()

b.normalMove(b.board, 0 , 2, 2, 0)
#def normalMove(self, board, x, y, pieceColor, direction):
#if (direction == 0 and pieceColor == 2): #red move down right
b.printBoard(b.board)



