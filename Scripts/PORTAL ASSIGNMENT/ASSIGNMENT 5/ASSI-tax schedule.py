'''
Task 1: Calculate Tax
Compute the taxes given the marital status and an income figure:
Federal Tax Schedule
If your status is single and your
taxable income is
Tax is Of the amount over
At most $32000 10% $0
More than $32000 $3200 + 25% $32000
If your status is married and
your taxable income is
Tax is Of the amount over
At most $64000 10% $0
More than $64000 $6400 + 25% $64000

THE PROGRAM SHOULD INPUT THE MARITAL STATUS AND YEARLY INCOME OF THE
INDIVIDUAL/COUPLE AND COMPUTE THE TAZES AS PER THE ABOVE SCHEDULE 

'''

RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0


income = float(input("Enter your income :  "))
maritalStatus = input("Enter s for single, m for married : ")

tax1 = 0
tax2 = 0

if maritalStatus == "s" :
    if income <= RATE1_SINGLE_LIMIT :
        tax1 = RATE1 * income
    else : 
        tax1 = RATE1 * RATE1_SINGLE_LIMIT 
        tax2 = RATE2 * ( income - RATE1_SINGLE_LIMIT)
else :
    if income <= RATE1_MARRIED_LIMIT :
        tax1 = RATE1 * income
    else :
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)
totalTax = tax1 + tax2

print("The tax is ", totalTax)