## Write the code as per the given test cases

'''
Mayuri buys “N” no of products from a
Shop. The shop offers a different percentage of discount on
each item. She
Wants to know the item that has the minimum discount offer,
so that she can
Avoid buying that and save money.
[Input Format: The first input refers to the no of items; the
second input is
the item name, price and discount percentage separated by
comma(,)]
Assume the minimum discount offer is in the form of Integer.
Note: There can be more than one product with a minimum
discount.
Sample Input 1:
4

2

Mobile, 10000, 20
Shoe, 5000, 10
Watch, 6000, 15
Laptop, 35000, 5
Sample Output 1:
Shoe
Explanation: The discount on the mobile is 2000, the discount
on the shoe is
500, the discount on the watch is 900 and the discount on the
laptop is 1750.
So the discount on the shoe is the minimum.
Sample Input 2:
4
Mobile, 5000, 10
Shoe, 5000,10
WATCH, 5000, 10
Laptop, 5000, 10
Sample Output 2:
Mobile
Shoe
WATCH
Laptop

'''
items = int(input())
itemList=[]
for i in range(items):
    itemList.append(input().split(","))
list2=[]
for i in itemList:
    i.append((int(i[1])*int(i[2]))//100)
    list2.append(i[3])
result=[]  
minimum = min(list2)
for i in itemList:
    if i[3] == minimum:
        result.append(i[0])
for i in result:
    print(i)