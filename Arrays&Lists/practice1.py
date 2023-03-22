def double(arr):
    arr1=[]
    n=len(arr)*2
    for i in range(n):
        if i< len(arr):
            arr1.append(arr[i])
        else:
            arr1.append(arr[n-i])
    
    
arr = [1,2,3]
double(arr)