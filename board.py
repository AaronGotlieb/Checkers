'''
Aaron Gotlieb
board object
'''

from piece import *

class board(object):
	def __init__(self, boardArray):
		self.boardArray = self.makeBoard()
		self.boardArray = self.setUp(self.boardArray)

	def printBoard(self):
		print ('   0 1 2 3 4 5 6 7  x')
		print('')
		for x in range (0, 8):
			print(x, end= '  ')
			for y in range (0, 8):
				print(self.boardArray[x][y].getColor(), end=' ')
			print('')
		print('y')

	def getBoardArray(self):
		return self.boardArray

	def getSquare(self, x, y):
		self.boardArray[x][y].printPiece()

	def addPiece(self, board, x, y, color):
		if (self.board[x][y] == 0):
			print('not legal move!')
			return
		self.board[x][y] = color

	def removePiece(self, board, x, y):
		if (self.board[x][y].getColor() == 0):
			print('not legal move!')
			return
		self.board[x][y].changeColor(0)

	def normalMove(self, board, x, y, pieceColor, direction):
		self.removePiece(board, x, y)
		if (direction == 0 and pieceColor == 2): #red move down right
			self.addPiece(board, x + 1, y + 1, pieceColor)

	def setUp(self, board):
	# sets up checkers board with 'r' and 'b' representing red and black respectivly

		for y in range (0, 8):
			for x in range (0, 3):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y].changeColor('r')
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y].changeColor('r')
		for y in range (0, 8):
			for x in range (5, 8):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y].changeColor('b')
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y].changeColor('b')
		return board

	def pieceArray(self, color):
		#(self, x, y, isKing, pieceColor)
		arr = [0 for x in range(8)]
		for x in range (0, 8):
			arr[x] = piece(0,0,0,color)
		return arr

	def makeBoard(self):
		board = [[0 for x in range(8)] for x in range(8)]
		for x in range (0, 8):
			for y in range (0, 8):
				if (x % 2 == 1):
					if (y % 2 == 1):
						board[x][y] = piece(x,y,0,0,0)
					else:
						board[x][y] = piece(x,y,0,0,1)
				else:
					if (y % 2 == 1):
						board[x][y] = piece(x,y,0,0,1)
					else:
						board[x][y] = piece(x,y,0,0,0)
		return board




