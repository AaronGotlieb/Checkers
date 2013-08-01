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

	def getPiece(self):
		return (self)

	def printPiece(self):
		print('Location: (' , self.x, ',' , self.y , ') Is King:' , self.isKing ,'Color:' , self.pieceColor, 'Square:', self.square)

	def changeLoc(self, newLoc):
		self.loc = newLoc

	def changeKing(self, newIsKing):
		self.isKing = newIsKing

	def changeColor(self, newColor):
		self.pieceColor = newColor

	def changePlayer(self, newPlayer):
		self.player = newPlayer

	def getColor(self):
		return (self.pieceColor)

	def getSquare(self):
		return (self.square)

	def changeSquare(self, newSquare):
		self.square = newSquare



