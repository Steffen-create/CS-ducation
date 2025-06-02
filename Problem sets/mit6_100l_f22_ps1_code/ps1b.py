## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary: float = float(input("Enter your yearly salary: "))
portion_saved: float = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home: float = float(input("Enter the cost of your dream home: "))
semi_annual_raise: float = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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
    months += 1
    interest = amount_saved * r / 12
    amount_saved += interest + portion_saved * yearly_salary / 12
    if months%6 == 0:
        yearly_salary *= (1 + semi_annual_raise)

print(f"Number of months: {months}")