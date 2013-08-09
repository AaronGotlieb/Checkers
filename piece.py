'''
Aaron Gotlieb
piece object
'''

class piece(object):
	def __init__(self, x, y, isKing, pieceColor, square):
		self.x = x
		self.y = y
		self.isKing = isKing
		self.pieceColor = pieceColor
		self.square = square
		self.openSpots = [0,0,0,0]

	def getPiece(self):
		return (self)

	def getColor(self):
		return (self.pieceColor)
		#return (self.isKing)

	def getSquare(self):
		return (self.square)

	def getOpenSpots(self):
		return (self.openSpots)

	def getIsKing(self):
		return (self.isKing)

	def changeSquare(self, newSquare):
		self.square = newSquare

	def changeLoc(self, newLoc):
		self.loc = newLoc

	def changeKing(self, newIsKing):
		self.isKing = newIsKing

	def changeColor(self, newColor):
		self.pieceColor = newColor

	def changePlayer(self, newPlayer):
		self.player = newPlayer

	def resetSquare(self):
		self.isKing = 0
		self.pieceColor = 0
		tmp = self.openSpots
		tmp = len(tmp)
		for x in range (0, tmp):
			self.openSpots[x] = 0

	def printPiece(self):
		print('Location: (' , self.y, ',' , self.x , ') Is King:' , self.isKing ,'Color:' , self.pieceColor, 'Square:', self.square, 'openSpots:', self.openSpots)

#avaiable moves
	def topLeft(self, topLeft):
		self.openSpots[0] = topLeft

	def topRight(self, topRight):
		self.openSpots[1] = topRight

	def botLeft(self, botLeft):
		self.openSpots[2] = botLeft

	def botRight(self, botRight):
		self.openSpots[3] = botRight

	def avaliableTranslate(self, allAvaliable):
		self.openSpots = allAvaliable




