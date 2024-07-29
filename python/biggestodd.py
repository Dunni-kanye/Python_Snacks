def biggest_odd(numbers_str):
	numbers = [int(num) for num in numbers_str.split()]

	odd_numbers = [num for num in numbers if num % 2 != 0]
	if odd_numbers:
		return max(odd_numbers)

	else:
		return invalid

print(biggest_odd("2 3 5 6 9"))
	