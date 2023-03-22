def second_largest(arr):
    largest=float('-inf')
    second_largest = float('-inf')
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i 
        elif (i>second_largest) and (i!=largest):
            second_largest = i
    return second_largest


arr =[12,54,34,23,11,6]
res=second_largest(arr)
print(res)