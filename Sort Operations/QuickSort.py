def quicksort(a):
    if len(a) <= 1:
        return a
    pivot=a[0]
    left=[]
    right=[]
    for i in range(1,len(a)):
        if a[i]<pivot:
            left.append(a[i])
        else:
            right.append(a[i])

    return quicksort(left)+[pivot]+quicksort(right)          




a=[3,1,22,12,56,78,23]

r=quicksort(a)
print(r)