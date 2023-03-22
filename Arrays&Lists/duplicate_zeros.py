def duplicate_zeros(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr.pop()
            arr.insert(i+1, 0)
            i += 1
        i += 1
        
    return arr

arr=[1,0,2,3,0,4,5,0]
x=duplicate_zeros(arr)
print(x)