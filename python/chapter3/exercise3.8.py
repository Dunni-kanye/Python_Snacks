number1 = int(input('Enter first integer:'))
number2 =int(input('Enter second integer:'))
number3 =int(input('Enter third integer:'))
number4 =int(input('Enter fourth integer:'))

for number in range(1,5):


	sum = number1 + number2 + number3 + number4 
	print(sum)
	
	average = number1 + number2 + number3 + number4 / 4
	print(average) 

	product = number1 * number2 * number3 *number4
	print(product)

	if  number1 < number2 and number1 < number3 and number1 < number4:
		print('number1 = smallest number')

	if number2 < number1 and number2 < number3 and number2 < number4:
		print('number2 = smallest number')

	if number3 < number1 and number3 < number2 and number3 < number4:
		print('number3 = smallest number')
	if number4 < number1 and number4 < number2 and number4 < number3:
		print('number4 = smallest number')

	if  number1 > number2 and number1 > number3 and number1 > number4:
		print('number1 = largest number')

	if number2 > number1 and number2 > number3 and number2 > number4:
		print('number2 = largest number')

	if number3 > number1 and number3 > number2 and number3 > number4:
		print('number3 = largest number')

	if number4 > number1 and number4 > number2 and number4 > number3:
		print('number4 = largest number')