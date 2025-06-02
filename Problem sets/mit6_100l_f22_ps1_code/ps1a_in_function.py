def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	months = 0
	portion_down_payment = 0.25
	down_payment = portion_down_payment * cost_of_dream_home
	amount_saved = 0
	r = 0.05
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < down_payment:
	    interest = amount_saved * r / 12
	    amount_saved += interest + portion_saved * yearly_salary / 12
	    months += 1
	
	print(f"Number of months: {months}")
	return months