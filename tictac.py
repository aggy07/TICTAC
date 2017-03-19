from __future__ import print_function

choices = []

for x in range(0,9):
	choices.append(str(x+1))

playerOneTurn = True
winner = False

def printBoard():
	print('\n ____')
	print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] +'|')
	print(' ____')
	print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] +'|')
	print(' ____')
	print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
	print(' ____\n')

while not winner:
	printBoard()

	if playerOneTurn:
		print('Player1')
	else:
		print('Player2')

	try:
		choice = int(raw_input(">>"))
	except:
		print("Please enter a valid field")
	if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
		print("illegal move, plase try again")
		continue
	if playerOneTurn:
		choices[choice - 1] = 'X'
	else:
		choices[choice - 1] = 'O'
	playerOneTurn = not playerOneTurn

	for x in range(0, 3):
		y = x * 3
		if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]):
			winner = True
			printBoard()
		if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]):
			winner = True
			printBoard()

	if ((choices[0] == choices[4] and choices[0] == choices[8]) or
			(choices[2] == choices[4] and choices[4] == choices[6])):
		winner = True
		printBoard()

print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")





