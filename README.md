Checkers
========

A Checkers game built in Python
	require Python 3.0


HUMAN interface:


	1) input (x,y) coordinates of the piece you want to move
		 (not the location you want to move to!)

	2) type the direction you want to move the pice
		 4 allowed inputs [topLeft, topRight, botLeft, botRight]

	bonus example:
		 if you want to move the red peice at point (0,2) to point (1,3)
		 the input would be '0' (enter/return) '2' (enter/return)  'botRight'
		 (enter/return)

		 well done!


inheritance diagram:


	main.py
  		 \
		board.py
    		\
			piece.py


Piece state codes:

	square:
		0 = red
		1 = black

	Direction:
		0 = right
		1 = left

	pieceColor:
		0 = not a piece and unavaliable move
		1 = not a piece but avaliable move
		r = red
		b = black

	isKing:
		0 = no
		1 = yes

	openSlots:
		openSlots = [0,0,0,0]
		0 = not avaliable move
		1 = avaliable move

		openSlots = [topLeft, topRight, botLeft, botRight]

Board:

	alpha 0.1:
		*****
		r 0 r 0 r 0 r 0
		0 r 0 r 0 r 0 r
		r 0 r 0 r 0 r 0
		0 0 0 0 0 0 0 0
		0 0 0 0 0 0 0 0
		0 b 0 b 0 b 0 b
		b 0 b 0 b 0 b 0
		0 b 0 b 0 b 0 b
		*****

	alpha 0.2:
		   0 1 2 3 4 5 6 7

		0  r 0 r 0 r 0 r 0
		1  0 r 0 r 0 r 0 r
		2  r 0 r 0 r 0 r 0
		3  0 0 0 0 0 0 0 0
		4  0 0 0 0 0 0 0 0
		5  0 b 0 b 0 b 0 b
		6  b 0 b 0 b 0 b 0
		7  0 b 0 b 0 b 0 b



