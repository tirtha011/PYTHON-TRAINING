# Detect if a input number is divisible by 7

num = int(input("enter number"))
if num % 7 == 0:
    print("{} is divisible!".format(num))
else:
    print("{} is not divisible!".format(num))
