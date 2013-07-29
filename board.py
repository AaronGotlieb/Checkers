'''
Aaron Gotlieb
board object
'''
class board(object):
	def __init__(self):
		board = [[0 for x in range(8)] for x in range(8)]

	def printBoard(self):
		print(self)

	def getBoard(self):
		board = [[1 for x in range(8)] for x in range(8)]
		for x in range (0, 8):
			for y in range (0, 8):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y] = 0
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y] = 0
		return board


