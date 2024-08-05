from array import *
arr = array('i', [])
length = int(input("Enter the length of the array:"))
for i in range (length):
	x = int(input("Enter the next value:"))
	arr.append(x)
print(arr)
