information = input("Type 'YES' for employee information:")
employee_name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked in a week:"))
hourly_pay_rate = float(input("Enter hourly pay rate:"))
federal_withholding_rate = float(input("Enter federal tax withholding rate:"))
state_tax_rate =float(input ("Enter state tax withholding rate:"))

gross_pay = hours_worked * hourly_pay_rate
federal_withholding = gross_pay * federal_withholding_rate
state_withholding = gross_pay * state_tax_rate
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction

print("\nPayroll Statement")
print(f'Employee Name: {employee_name}')
print(f'Hours Worked: {hours_worked}')
print(f'Pay Rate: {hourly_pay_rate}')
print(f'Federal Tax Withholding: {federal_withholding_rate}')
print(f'State Tax Rate: {state_tax_rate}')

print("Deductions:")
print(f'Federal Withholding(20.0%): {federal_withholding}')
print(f'State Withholding: {state_withholding}')
print(f'Total Deduction: {total_deduction}')
print(f'Net Pay: {net_pay}')









 

   