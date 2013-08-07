'''
Aaron Gotlieb
'''
import sys
from board import *
#from piece import *

print("Welcome to (zork)Checkers!")
print('You will be 1')
print("Ready Player 1")

# board/initial setup
arr = []
b = board(arr)

def coordinateCheck(letter):
	string = 'input %s coordinate: ' % letter
	while True:
		try:
			x = int(input(string))
		except ValueError:
			print("%s coordinate must be a number! (integer)" % letter)
			continue
		if (x > 8 or x < 0):
			print("%s coordinate must be between 0 and 7!" % letter)
		else:
			print('well done!')
			return(x)
def direction():
	print('now enter direction (topLeft, topRight, botLeft or botRight)')
	while True:
		d = str(input())
		if (d == 'topLeft' or d == 'topRight' or d == 'botRight' or d == 'botLeft'):
			print('well done!')
			return(d)
		else:
			print('please input one of the four choices  (topLeft, topRight, botLeft or botRight)')

def movePiece(x, y, direction):
	if (b.boardArray[x][y].getIsKing() == 0):
		b.normalMove(x,y,direction)
	else:
		b.royalMove(x,y,direction)

# game loop
while True:
	b.printBoard()
	print('enter a piece and where you want to move it.')
	x = coordinateCheck('x') # pass in name of number so its user identifiable
	y = coordinateCheck('y')
	direction = direction()
	#print(x , ' ' , y , ' ' , direction)
	movePiece(x,y,direction)
	b.printBoard()
	break
'''
#b.normalMove(2,2,'botLeft')
b.kingMove(2,0,'botRight')
b.kingMove(2,6, 'botRight')
b.kingMove(5,1,'topLeft')
b.kingMove(5,7,'topLeft')

b.printBoard()


for x in range (0,8):
	for y in range(0,8):
		b.getSquare(x,y)



#def normalMove(self, board, x, y, pieceColor, direction):
#if (direction == 0 and pieceColor == 2): #red move down right
'''


