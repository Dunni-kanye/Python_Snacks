return_value = 0.07
amount_invested = 1000
  
number_of_years = 30

p = amount_invested
n = number_of_years
r = return_value

for years in range(1,30):

	amounts_on_deposits = p*(1 + r) ** n
	amounts_on_deposit_for_30_years = 1000*(1 + 0.07)**years


	print(f"{amounts_on_deposit_for_30_years:.2f}")

