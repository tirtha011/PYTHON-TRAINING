def insertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp
 
 
list = input('Enter the list of numbers: ').split()
list = [int(x) for x in list]
insertionSort(list)
print('Sorted list: ', end='')
print(list)