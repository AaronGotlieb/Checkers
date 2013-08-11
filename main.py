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
		try:
			b.normalMove(x,y,direction)
		except Exception:
			print('Illegal move detected, please try again')
	else:
		try:
			b.royalMove(x,y,direction)
		except Exception:
			print('Illegal move detected, please try again')

# game loop
b.normalMove(2,4,'botLeft')
b.normalMove(2,6,'botLeft')
b.normalMove(5,5,'topRight')
b.printBoard()
print(b.normalTakeCheck(6,4))
'''
while True:
	x = y = direc = 0
	b.printBoard()
	print('enter a piece and where you want to move it.')
	x = coordinateCheck('x') # pass in name of number so its user identifiable
	y = coordinateCheck('y')
	direc = direction()
	#print(x , ' ' , y , ' ' , direction)
	try:
		movePiece(y,x,direc)
	except Exception:
		print('Illigal move detected, please try again')
		continue
	b.printBoard()
	break

for x in range (0,8):
	for y in range(0,8):
		b.getSquare(x,y)

#b.normalMove(2,2,'botLeft')
b.normalMove(2,0,'botRight')
b.royalMove(2,6, 'botRight')
b.royalMove(5,1,'topLeft')
b.royalMove(5,7,'topLeft')

b.printBoard()


for x in range (0,8):
	for y in range(0,8):
		b.getSquare(x,y)



#def normalMove(self, board, x, y, pieceColor, direction):
#if (direction == 0 and pieceColor == 2): #red move down right
'''


