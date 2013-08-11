'''
Aaron Gotlieb
board object
'''

from piece import *

class board(object):
	def __init__(self, boardArray):
		self.boardArray = self.makeBoard()
		self.boardArray = self.setUp(self.boardArray)
		self.openMoves()

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

	def openMoves(self):
		# checks what moves are open for all pieces and updates the each piece object to represent
		# what moves are available within the piece object under 'openSpots'
		# example output: [0, 0, 0, 0, 1, 3, 3, 3]
		for x in range (0, 8):
			for y in range (0, 8):
				if (x+1 > 7 or y+1 > 7):
					self.boardArray[x][y].botRight(0)
				elif(self.boardArray[x+1][y+1].getColor() == 1): # is an empty square bottom right
					self.boardArray[x][y].botRight(1)
				else:
					self.boardArray[x][y].botRight(0)

				if(x+1 > 7 or y-1 < 0):
					self.boardArray[x][y].botLeft(0)
				elif(self.boardArray[x+1][y-1].getColor() == 1): # is an empty square bottom left
					self.boardArray[x][y].botLeft(1)
				else:
					self.boardArray[x][y].botLeft(0)

				if(x-1 < 0 or y+1 > 7):
					self.boardArray[x][y].topRight(0)
				elif(self.boardArray[x-1][y+1].getColor() == 1): # is an empty square top right
					self.boardArray[x][y].topRight(1)
				else:
					self.boardArray[x][y].topRight(0)

				if(x-1 < 0 or y-1 < 0):
					self.boardArray[x][y].topLeft(0)
				elif(self.boardArray[x-1][y-1].getColor() == 1): # is an empty square top left
					self.boardArray[x][y].topLeft(1)
				else:
					self.boardArray[x][y].topLeft(0)
				self.openMovesTranslator(x,y)

	def royalMove(self, x, y, direction):
		self.openMoves()
		openSpots = self.boardArray[x][y].getOpenSpots()
		if(direction == 'topLeft'):
			openSpots = openSpots[0:2]
			if(openSpots[0] == -1 and openSpots[1] == -1):
				raise Exception('Sorry, but that move is illegal')
		if(direction == 'topRight'):
			openSpots = openSpots[2:4]
		if(direction == 'botLeft'):
			openSpots = openSpots[4:6]
		if(direction == 'botRight'):
			openSpots = openSpots[6:8]

		#actual move
		a = self.boardArray[x][y].getColor()
		b = self.boardArray[x][y].getSquare()
		self.boardArray[x][y].resetSquare()
		self.boardArray[openSpots[1]][openSpots[0]] = piece(openSpots[1],openSpots[0],1,a,b)
		self.openMoves()

	def normalTakeCheck(self, x, y):
		myColor = self.boardArray[x][y].getColor()
		if(myColor == 'r'):
			if(self.boardArray[y+1][x+1].getColor() == 'b' or self.boardArray[y+1][x-1].getColor() == 'b'): # 1 search ahead
				if(self.boardArray[x+2][y+2].getColor() == 1 or self.boardArray[y+2][x-2].getColor() == 1):
					return True
		else:
			if(myColor == 'b'):
				if(self.boardArray[y-1][x+1].getColor() == 'r' or self.boardArray[y-1][x-1].getColor() == 'r'): # 1 search ahead
					if(self.boardArray[x-2][y+2].getColor() == 1 or self.boardArray[y-2][x-2].getColor() == 1):
						return True
		return False

	def normalTake(self,x,y,direction):
		myColor = self.boardArray[x][y].getColor()
		if(self.normalTakeCheck(x,y) == False)
			raise Exception('Sorry, but the move you are attempting is illegal')
		if(myColor == 'r'):


		return True

	def normalMove(self, x, y, direction):
		#movement rules
		self.openMoves()
		openSpots = self.boardArray[x][y].getOpenSpots()

		if(direction == 'topLeft'):
			openSpots = openSpots[0:2]
			if(openSpots[0] == -1 and openSpots[1] == -1):
				raise Exception('Sorry, but that move is illegal')
		if(direction == 'topRight'):
			openSpots = openSpots[2:4]
		if(direction == 'botLeft'):
			openSpots = openSpots[4:6]
		if(direction == 'botRight'):
			openSpots = openSpots[6:8]
		if(self.boardArray[x][y].getIsKing() == 0): #not king
			if(self.boardArray[x][y].getColor() == 'r'): #red
				if(direction == 'topLeft' or direction == 'topRight'):
					raise Exception('Sorry, but that move is illegal')
			if(self.boardArray[x][y].getColor() == 'b'): #black
				if(direction == 'botRight' or direction == 'botLeft'):
					raise Exception('Sorry, but that move is illegal')
		tmp = self.boardArray[0][0].getIsKing  # really hacky way of taking care of the [0][0]
		self.boardArray[0][0].changeKing(1337) # special case...
		if(openSpots[0] == 0 and openSpots[1] == 0 and self.boardArray[openSpots[1]][openSpots[0]].getIsKing != 1337):
			raise Exception('Sorry, but that move is illegal')
		self.boardArray[0][0].changeKing(tmp)
		# more tests will be needed above but for now...
		# actual move
		a = self.boardArray[x][y].getColor()
		b = self.boardArray[x][y].getSquare()
		self.boardArray[x][y].resetSquare()
		self.boardArray[openSpots[1]][openSpots[0]] = piece(openSpots[1],openSpots[0],0,a,b)
		self.openMoves()

	def openMovesTranslator(self, x, y):
		# openSlots = [topLeft, topRight, botLeft, botRight]  <== copied from readme
		tmp = [0,0,0,0,0,0,0,0]
		avaliable = self.boardArray[x][y].getOpenSpots()
		if (avaliable[0] == 1): #top left available
			tmp[0] = y-1
			tmp[1] = x-1
		if (avaliable[1] == 1): #top right available
			tmp[2] = y+1
			tmp[3] = x-1
		if (avaliable[2] == 1): #bot left available
			tmp[4] = y-1
			tmp[5] = x+1
		if (avaliable[3] == 1): #bot right available
			tmp[6] = y+1
			tmp[7] = x+1
		self.boardArray[x][y].avaliableTranslate(tmp)

	def setUp(self, board):
	# sets up checkers board with 'r' and 'b' representing red and black respectively
		for y in range (0, 8):
			for x in range (0,8):
				if (y % 2 == 1 and x % 2 == 1):
					board[x][y].changeColor(1)
				if (y % 2 == 0 and x % 2 == 0):
					board[x][y].changeColor(1)

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
		# def __init__(self, x, y, isKing, pieceColor, square): <== pieces constructor
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



