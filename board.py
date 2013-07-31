'''
Aaron Gotlieb
board object
'''

from piece import *

class board(object):
	def __init__(self):
		'''
		self.board = [[0 for x in range(8)] for x in range(8)]
		tmp = [[0 for x in range(8)] for x in range(8)]
		for x in range (0, 8):
			for y in range (0, 8):
				if (y % 2 == 1 and x % 2 == 1):
					tmp[x][y] = 1
				if (y % 2 == 0 and x % 2 == 0):
					tmp[x][y] = 1
		self.board = tmp
		'''
		tmp = self.makeBoard()
		for x in range (0, 8):
			print(tmp[x])
		tmp = self.setUp(tmp)
		print('flagOne')

	def printBoard(self, board):
		print ('*****')
		for x in range (0, 8):
			print('')
			for y in range (0, 8):
				if (y % 2 == 1 and x % 2 == 1):
					if (board[x][y] == 0 or board[x][y] == 1 or board[x][y] == 2 or board[x][y] == 3):
						print(board[x][y], end=' ')
					else:
						print (board[x][y].getColor(), end=' ')
				elif (y % 2 == 0 and x % 2 == 0):
					if (board[x][y] == 0 or board[x][y] == 1 or board[x][y] == 2 or board[x][y] == 3):
						print(board[x][y], end=' ')
					else:
						tmp = board[x][y]
						print(tmp.getColor(), end=' ')
						#print (board[x][y].getColor, end=' ')
		print('')
		print ('*****')

	def getBoard(self):
		return self.board

	def addPiece(self, board, x, y, color):
		if (self.board[x][y] == 0):
			print('not legal move!')
			return
		self.board[x][y] = color

	def removePiece(self, board, x, y):
		if (self.board[x][y] == 0):
			print('not legal move!')
			return
		self.board[x][y] = 1

	def normalMove(self, board, x, y, pieceColor, direction):
		self.removePiece(board, x, y)
		if (direction == 0 and pieceColor == 2): #red move down right
			self.addPiece(board, x + 1, y + 1, pieceColor)
			print("flag")

	def setUp(self, board):
	# sets up checkers board with 2 and 3 representing red and black respectivly

		board = self.makeBoard()
		redPieces = self.pieceArray(2)
		blackPieces = self.pieceArray(3)

		for y in range (0, 8):
			for x in range (0, 3):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y] = redPieces[x].getColor()
				elif (y % 2 == 0 and x % 2 == 0):
					board[x][y] = redPieces[x].getColor()
		for y in range (0, 8):
			for x in range (5, 8):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y] = blackPieces[x].getColor()
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y] = blackPieces[x].getColor()
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
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y] = 1
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y] = 1
		return board

'''
board inicilization:
				j = [[0 for x in range(8)] for x in range(8)]
		for x in range (0, 8):
			for y in range (0, 8):
				if (y % 2 == 1 and x % 2 == 1):
					j[x][y] = 1
				if (y % 2 == 0 and x % 2 == 0):
					j[x][y] = 1
		self.board = j
'''



