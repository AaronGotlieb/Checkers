'''
Aaron Gotlieb
piece object
'''

class piece(object):
	def __init__(self, loc, isKing, color, player):
		self.loc = loc
		self.isKing = isKing
		self.color = color
		self.player = player

	def getPiece(self):
		return (self)

	def printPiece(self):
		print self.loc
		print self.isKing
		print self.color
		print self.player
		print (self.loc + self.isKing + self.color + self.player)

	def changeLoc(self, newLoc):
		self.loc = newLoc

	def changeKing(self, newIsKing):
		self.isKing = newIsKing

	def changeColor(self, newColor):
		self.color = newColor

	def changePlayer(self, newPlayer):
		self.player = newPlayer
