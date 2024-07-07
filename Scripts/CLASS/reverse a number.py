#program to reverse the input number

#input 
userNam = input("Enter an integer : ")

#process
if (userNam.isdigit()):
    print ( "The reversed number is ", userNam[ ::-1])
else:
    print("The input is not a number")

