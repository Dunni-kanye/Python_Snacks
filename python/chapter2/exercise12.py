return_value = 0.07
amount_invested = 1000
  
number_of_years = 10

p = amount_invested
n = number_of_years
r = return_value

amounts_on_deposits = p*(1 + r) ** n
amounts_on_deposit_for_10_years = 1000*(1 + 0.07)**10

number_of_years = 20

amounts_on_deposit_for_20_years = 1000*(1 + 0.07)**20

number_of_years = 30

amounts_on_deposit_for_30_years = 1000*(1 + 0.07)**30


print(f"{amounts_on_deposit_for_10_years:.2f}")

print(f"{amounts_on_deposit_for_20_years:.2f}")

print(f"{amounts_on_deposit_for_30_years:.2f}")

