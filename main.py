'''
Aaron Gotlieb
'''

from board import *
#from piece import *

print("Welcome to (zork)Checkers!")
print("Ready Player 1")
arr = []
b = board(arr)
print(b)
b.printBoard()

#b.normalMove(2,2,'botLeft')
b.normalMove(2,0,'botRight')
b.normalMove(2,6, 'botRight')
b.normalMove(5,1,'topLeft')
b.normalMove(5,7,'topLeft')

b.printBoard()


for x in range (0,8):
	for y in range(0,8):
		b.getSquare(x,y)



#def normalMove(self, board, x, y, pieceColor, direction):
#if (direction == 0 and pieceColor == 2): #red move down right



