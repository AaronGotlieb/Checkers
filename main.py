'''
Aaron Gotlieb
'''

from board import *
#from piece import *

print("Welcome to (zork)Checkers!")
print("Ready Player 1")
arr = [[0 for x in range(8)] for x in range(8)]
j = 'nothing'
b = board(arr)
arr = b.getBoardArray()
print("flag1")
print(b)
b.printBoard(b)

#def normalMove(self, board, x, y, pieceColor, direction):
#if (direction == 0 and pieceColor == 2): #red move down right



