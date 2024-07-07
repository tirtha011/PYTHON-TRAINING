#program to input a number nd detect if it is prime or not

#input 
n = int(input("Enter a number: "))

#process
for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
    
else:
    print("The number is prime")