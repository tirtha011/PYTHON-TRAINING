# Task 1: Write code and pass the test cases.
'''
 Easy
You are playing an online game. In the game, a list of N numbers is
given. The player has to arrange the numbers so that all the odd
numbers of the list come after the even numbers. Write an algorithm
to arrange the given list such that all the odd numbers of the list
come after the even numbers.
Input

The first line of the input consists of an integer num, representing
the size of the list(N). The second line of the input consists of N
space-separated integers representing the values of the list

Output

Print N space-separated integers such that all the odd numbers of
the list come after the even numbers

Example

Sample Input
8
10 98 3 33 12 22 21 11
Sample Output
10 98 12 22 3 33 21 11
Explanation
All the even numbers are placed before all the odd numbers.
Solution
Input
8
15 16 14 17 18 19 20 11

'''

n=int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
while left < right:
    while(arr[left] % 2 == 0 and left < right):
        left = left + 1
    while(arr[right] % 2 == 1 and left < right):
        right = right - 1
    if (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left = left + 1
        right = right - 1
        
for i in range (0, n):
    print(arr[i], end = ' ')