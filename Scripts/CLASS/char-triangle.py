#program to create a character triangle

#input 
#    c -> character (*)
#    l -> 3
#output
#    *
#    **
#    ***

#input
print(" This program prints a character triangle")
ch = input("Enter the character: ")
line = int(input("Enter the number of lines : "))


#process
for i in range(1, line, +1):
     # for reverse-> for i in range(line, 0, -1)
    print(ch*i)

#output