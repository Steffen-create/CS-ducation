## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary: float = float(input("Enter your yearly salary: "))
portion_saved: float = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home: float = float(input("Enter the cost of your dream home: "))


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
    interest = amount_saved * r / 12
    amount_saved += interest + portion_saved * yearly_salary / 12
    months += 1

print(f"Number of months: {months}")