def Quicksort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left=[]
    right=[]
    for i in range(1,len(a)):
        if a[i]<pivot:
            left.append(a[i])
        else:
            right.append(a[i])    
    return Quicksort(left)+[pivot]+Quicksort(right)        


a=[334,32,2,44,2334,342,78,6,1]
r=Quicksort(a)
print(r)