from array import *
arr = array('i', [])
length = int(input("Enter the length of the array:"))
for i in range (length):
	x = int(input("Enter the next value:"))
	arr.append(x)
print(arr)
val = int(input("Enter the value for search:"))
k = 0
for length in arr:
	if length == val:
		print(k)
		break
		
	else:
		k += 1
		