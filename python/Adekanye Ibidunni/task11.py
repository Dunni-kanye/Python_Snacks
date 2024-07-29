number = int(input("Enter a number:"))

divisible_by_5 = number % 5 == 0
divisible_by_6 = number % 6 == 0
if divisible_by_5 and divisible_by_6:
	print(f'{number}divisible by 5 and 6.')
elif divisible_by_5 or divisible_by_6:
	print(f'{number}divisible by 5 or 6.')
if divisible_by_5 != divisible_by_6:
	print(f'{number}divisible by 5 or 6,but not both.')





