## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit: float = float(input("enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_home = 800000
down_payment = 800000 * 0.25
epsilon = 100
months = 3 * 12
low = 0
high = 1
r = (high + low) / 2
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

def compound_interest(r: float, months: int, inital_deposit: float) -> float:
    return inital_deposit * ((1 + r/12)**months)

while abs(compound_interest(r, months, initial_deposit) - down_payment) > epsilon:
    if compound_interest(1, months, initial_deposit) < (down_payment - epsilon):
        r = None
        break
    if compound_interest(r, months, initial_deposit) - down_payment > epsilon:
        high = r
    else:
        low = r
    r = (high + low) / 2
    steps += 1
    if steps > 1000:
        print("more than 1000")
if r == None:
    print(f"Best savings rate: {r}")
else:
    print(f"Best savings rate: {r} [or very close to this number]")
print(f"Steps in bisection search: {steps} [May vary based on how you implemented your bisection search]")