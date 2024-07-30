final_account_value = 5000
monthly_interest_rate = float(input("Enter the interest rate:"))

number_of_years = 3

initial_deposit_amount = final_account_value / (1 + monthly_interest_rate) ** number_of_years

print(f'{initial_deposit_amount:.2f}')
