r = 0.04
annual_salary = int(input("Enter your annual salary: "))

total_cost = 1000000
semi_annual_raise = 0.07


portion_down_payment = .25	* total_cost


monthly_savings_range = [0,10000]

monthly_savings_percent = 0
current_savings = 0
bisection_counter = 1
while abs(current_savings - portion_down_payment) >100:
	current_savings = 0
	
	monthly_savings_percent = float(monthly_savings_range[0] + monthly_savings_range[1])/20000
	monthly_savings_percent = float(int(monthly_savings_percent*10000))/10000

	salary_saved = monthly_savings_percent*annual_salary/12

	for idx in range(1, 37):

		current_savings = current_savings*(1+r/12) +  salary_saved

		#this if statement handles the raise
		if idx%6 == 0:
			salary_saved = salary_saved*(1+semi_annual_raise)

	if current_savings > (portion_down_payment + 100):
		monthly_savings_range[1] = int(monthly_savings_percent*10000)
		bisection_counter += 1 
		pass
		#print("we're doing if")
	elif current_savings < (portion_down_payment -100):
		monthly_savings_range[0] = int(monthly_savings_percent*10000)
		bisection_counter += 1 
		pass
		#print("we're doing elif")
	
	else: 
		
		print("Best savings rate:", monthly_savings_percent)
		print("Steps in bisection search:", bisection_counter)
		break
	print(monthly_savings_percent)





