'''
 Double the amount
Write a python program to calculate the number of years to double the invested amount
given the amount invested in INR and interest given in percentage per annum.
The program should input investment amount and interest rate. It should output the
number of years required to double the invested amount.

'''


interest_rate = int(input("Enter the interest rate : "))
print()
initial_investment = float(input("Enter the initial investment : "))
total = initial_investment
double = 2 * initial_investment
years = 0
while total < double:
    total += total * interest_rate
years +=1
print(f"Investment will take {years} years to double")