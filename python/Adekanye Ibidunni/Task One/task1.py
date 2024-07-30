#Prompt a user to read in the radius of a cylinder  
#let user also read in length of a cylinder
#prompt user to calculate the area and use area = pie(3.142)* radius **2 to #get the area.
#let user to calculate the volume using formula volume = area * length.
#print the result.



radius = int (input("Enter the value of radius:"))

length = int (input("Enter the value of length:"))

Pi = 3.142
area = pie * radius **2
volume = area * length

print(f'{area:.2f}')
print(f'{volume:.2f}')
