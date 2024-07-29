minutes = int(input("Enter the minutes:"))
total_minutes_in_a_year = 525600
total_minutes_in_a_day = 1440
year = minutes // total_minutes_in_a_year
remaining_minutes = minutes % total_minutes_in_a_year
day = year % total_minutes_in_a_day 

print(f'{year}{"years"} {"and"} {day}{"days"}')