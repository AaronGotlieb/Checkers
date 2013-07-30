'''
Aaron Gotlieb
board object
'''

class board(object):
	def __init__(self, board):
		j = [[1 for x in range(8)] for x in range(8)]
		for x in range (0, 8):
			for y in range (0, 8):
				if (y % 2 == 1 and x % 2 == 1):
					j[x][y] = 0
				if (y % 2 == 0 and x % 2 == 0):
					j[x][y] = 0
		self.board = j

	def printBoard(self):
		print(self.board)

	def getBoard(self):
		return self.board

	def addPiece(self, board, x, y, color):
		if (self.board[x][y] == 0):
			return 'not legal move!'
		self.board[x][y] = color
		return self.board

	def makeBoard(self, arr):
		board = [[1 for x in range(8)] for x in range(8)]
		for x in range (0, 8):
			for y in range (0, 8):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y] = 0
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y] = 0
		return board




