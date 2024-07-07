'''
: Write the code as per the given test cases
Problem Statement
Bela teaches her daughter to find the
Factors of a given number. When she provides a number to her daughter, she
3
Should tell the factors of that number. Help her to do this, by writing a
Program. Write a class FindFactor.java and write the main method in it.
Note:
● if the input provided is negative, ignore the sign and provide the output.
If the input is zero
● if the input is zero the output should be “No Factors”.
Sample Input 1:
54
Sample Output 1:
1, 2, 3, 6, 9, 18, 27, 54
Sample Input 2:
-1869
Sample Output 2:
1, 3, 7, 21, 89, 267, 623, 1869

'''
x = abs(int(input()))
if x == 0:
    print("No Factors")
    exit()
for i in range(1, x + 1):
    if x % i == 0:
        if i != x:
            print(i,end=", ")
        else:
            print(i)
