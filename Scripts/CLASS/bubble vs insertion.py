import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [random.randint(1, 1000) for i in range(1000)]

import time
start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time
start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

print("Bubble Sort time:", bubble_sort_time)
print("Insertion Sort time:", insertion_sort_time)

if ( bubble_sort_time > insertion_sort_time ):
    print ("Conclusion : Insertion Sort is faster " )
else :
    print("Conclusion : Bubble Sort is faster")