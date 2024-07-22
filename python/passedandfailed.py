no_of_students_passed = 0
no_of_students_failed = 0
	
for score in range (1, 15):
	score = int(input("Enter fifteen scores:"))
	if score >= 45:
		no_of_students_passed = no_of_students_passed + 1

	else:
		no_of_students_failed += 1
	
print('Passed is , ',no_of_students_passed)
print('Failed is , ',no_of_students_failed)

