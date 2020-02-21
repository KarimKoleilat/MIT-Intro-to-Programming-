r = 0.04
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home:")) 
semi_annual_raise = float(input("Enter semi-annual raise, as a decimal:"))


portion_down_payment = .25	* total_cost
current_savings = 0
salary_saved = portion_saved*annual_salary/12

months_counter = 0

while current_savings < portion_down_payment:
	months_counter += 1
		
	current_savings = current_savings*(1+r/12) +  salary_saved
	if months_counter%6 == 0:
		salary_saved = salary_saved*(1+semi_annual_raise)
	

print(months_counter)