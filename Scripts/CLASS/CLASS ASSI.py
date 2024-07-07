# write a function that will input some numbers and return the min and max of the set of numbers as a tuple 
# call -> getMinMax(1, 2, 3, 4, 6)
# output -> (1, 6)

def max_min(data):
    l = data[0] 
    s = data[0] 
    
    for num in data:
        if num > l:
            l = num 
        elif num < s:
            s = num  
    
    return l, s

print(max_min([1,2,3,4,6]))