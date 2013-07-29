'''
Aaron Gotlieb
'''

class makeBoard(board):
	board = [[0 for x in range(8)] for x in range(8)] 
	for x in range (0, 8):
		for y in range (0, 8):
			if (y % 2 == 1 and x % 2 == 1):
				board[x][y] = 1
			if (y % 2 == 0 and x % 2 == 0):
				board[x][y] = 1
	

class main():
	board
	board = makeBoard()

