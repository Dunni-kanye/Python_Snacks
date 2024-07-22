gallons = 0

while gallons != -1:

	gallons = float(input("Enter gallon used(-1 to end):"))
	if gallons == '-1':
		break

	miles = float(input("Enter the miles driven:"))
	
	tank = miles / gallons
 
	
	print(f"The miles/gallon for this tank was: {tank}")

