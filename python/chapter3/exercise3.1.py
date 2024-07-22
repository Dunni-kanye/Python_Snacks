number_of_passes = 0
number_of_failures = 0
value = ''
while value != '1' and value != '2':

	value = input("Enter either 1 or 2: ")


	if value =='1' or value == '2':
		print("valid: "  + value)

	else:
		number_of_failures += 1
		print("Invalid value,enter either 1 or 2.")	

print('Failed is , ',number_of_failures)
