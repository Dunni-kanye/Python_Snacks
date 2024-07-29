def only_floats(a, b):


	if type(a) == float and type(b) == float:
		return 2

	elif type(a) == float or type(b) == float:
		return 1

	else:
		return 0

	

print(only_floats(1.0, 2.0))
print(only_floats(9.0, 5))
print(only_floats(3, 6))
