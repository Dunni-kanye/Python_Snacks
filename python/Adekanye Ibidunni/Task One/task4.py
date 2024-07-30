#prompt a user
#let user input a value  and represent as subtotal 
#let user input a value in percentage and represent as gratuity rate
#covert the gratuity rate by multiplying by subtotal and divide by 100
#convert the subtotal by adding the value of the converted gratuity rate.
#print the result.


subtotal = int(input("Enter the subtotal value:"))
gratuity_rate =int( input("Enter the gratuity_rate value:"))

convert_gratuity_rate = subtotal * gratuity_rate / 100
convert_subtotal = subtotal + convert_gratuity_rate

print(convert_gratuity_rate)
print(convert_subtotal)
