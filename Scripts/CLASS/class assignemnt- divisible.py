#print all the numbers divisible by 7 and 11 between a given user input range



S = int(input("Enter a number: ")) #starting range
E = int(input("Enter a number: ")) #end range

for i in range(S,E+1):
    if (i%7 == 0 and i%11 == 0):
        print("The numbers are ", i)