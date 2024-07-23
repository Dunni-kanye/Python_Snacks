import math

def divide_or_square(number):
	if number % 5 == 0:
		return number**0.5


	else:
		return number % 5

print(divide_or_square(26))
print(divide_or_square(25))

	