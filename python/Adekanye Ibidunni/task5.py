#prompt the user
#let user give a range for 0 to 1000
#let user input an integer from 0 to 1000
#use the %operator to extract the input digits
#calculate the sum of the extracted digits
#print the result


value = int (input("Enter the value:"))
for value in range (0 - 1000):
	digit = num % 10 * value
	sum = value + digit

	print(sum)
