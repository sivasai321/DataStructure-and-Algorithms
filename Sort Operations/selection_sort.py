def selectionSort(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min] =a[min],a[i]   
    
    return a


arr=[2,4,1,42,7,21]    
r=selectionSort(arr)
print(r)