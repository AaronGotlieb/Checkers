Checkers
========

A Checkers game built in Python
	require Python 3.0

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



