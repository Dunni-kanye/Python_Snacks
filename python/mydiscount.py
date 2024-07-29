def my_discount(price, discount):

	discount_amount = price *(discount / 100)
	final_price = price - discount_amount
	return final_price


print(my_discount(150,15))