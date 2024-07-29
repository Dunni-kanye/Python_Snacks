from random import randint
 
start = input("Type 'YES' to play lottery:")
while start  in ['YES']:
	print('Guess three digit lottery number to play!')


	print('Guess a number from 900 - 999')

	lottery_number = int(input('Enter three digits number to be guessed:'))

	guess = randint(900,999 )
   
	print(f'{guess}')
	while lottery_number != guess:
		if lottery_number < guess:
			print('Too low, Try again!')
	
		elif lottery_number > guess:
			print('Too high, Try again!') 
		lottery_number = int(input('Enter three digits number to be guessed:'))


	if lottery_number == guess:
		print('You won $10,000')
	
	else:
		digits = set(str(lottery_number))
		one_digit = set(str(lottery_number))
		if digits == lottery_number:
			print('You won $3,000')
		elif one_digit == lottery_number:
			print('Sorry, you won $0!')
	start = input("Type 'YES' to play lottery again or 'NO' to end:")

print('closed!')
				


		
 

