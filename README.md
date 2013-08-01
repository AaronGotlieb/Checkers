Checkers
========

A Checkers game built in python

inheritance diagram:
	main.py <== board.py <== piece.py

Piece state codes:

	square:
		0 = red
		1 = black

	Direction:
		0 = right
		1 = left

	pieceColor:
		0 = not a piece
		r = red
		b = black

	isKing:
		0 = no
		1 = yes


Board:
	alpha 0.1
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
		all r / b / 0 are piece objects



