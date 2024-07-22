number1 = int(input('Enter first integer:'))
number2 =int(input('Enter second integer:'))
number3 =int(input('Enter third integer:'))

sum = number1 + number2 + number3 
print(sum)

average = number1 + number2 + number3 / 3
print(average) 

product = number1 * number2 * number3
print(product)

if  number1 < number2 and number1 < number3:
	print('number1 = smallest number')

if number2 < number1 and number2 < number3:
	print('number2 = smallest number')

if number3 < number1 and number3 < number2:
	print('number3 = smallest number')

if  number1 > number2 and number1 > number3:
	print('number1 = largest number')

if number2 > number1 and number2 > number3:
	print('number2 = largest number')

if number3 > number1 and number3 > number2:
	print('number3 = largest number')