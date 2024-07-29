from random import randint
start = input("Type 'YES' to start:")
while start  in ['YES']:
	print('Guess a number to play this game!')


	print('Guess a number from 1-1000')

	game = int(input('choose a number to be guessed:'))

	guess = randint(1,1001)

	while game != guess:
		
			if game < guess:
				print('Too low, Try again!')
	
			elif game > guess:
				print('Too high, Try again!')
			game = int(input('choose a number to be guessed'))
		


	print('Congratulations, you guessed the number!')

	start = input("Type 'YES' to play again or 'NO' to end:")

print('Game closed')
