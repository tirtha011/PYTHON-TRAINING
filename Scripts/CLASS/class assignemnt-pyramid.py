#Create a program to input a character and number of lines and build a character pyramid

char= input("Enter a character:")
lines = int(input("Enter the number of lines:"))
for i in range(1, lines + 1):
    print(" "*(lines-i),end=" ")
    print(char*i + char*(i-1))