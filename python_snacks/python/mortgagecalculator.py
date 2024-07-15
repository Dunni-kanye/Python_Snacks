

principal_amount= int(input('Enter the principal-amount:'))
annual_interest_rate= int(input('Enter the annual interest rate:'))
duration_in_years = int(input('Enter the duration in years:'))
p = principal_amount
r = annual_interest_rate / 100 /12 
n = duration_in_years * 12


monthly_payment= p * (r* (1+r)**n) / (((1+r)**n)-1)
print(monthly_payment)