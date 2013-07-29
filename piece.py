'''
Aaron Gotlieb
piece object
'''

class piece(object):
	def __init__(self, x, y, isKing, color, player):
		self.x = x
		self.y = y
		self.isKing = isKing
		self.color = color
		self.player = player

	def getPiece(self):
		return (self)

	def printPiece(self):
		print 'Location:' , self.x, ',' , self.y , 'Is King:' , self.isKing ,'Color:' , self.color , 'Player Number:' , self.player

	def changeLoc(self, newLoc):
		self.loc = newLoc

	def changeKing(self, newIsKing):
		self.isKing = newIsKing

	def changeColor(self, newColor):
		self.color = newColor

	def changePlayer(self, newPlayer):
		self.player = newPlayer


