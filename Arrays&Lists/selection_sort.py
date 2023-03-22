def selection_sort(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(a[j]<a[min]):
                min=j

        [a[i],a[min]]=[a[min],a[i]]

    return a        

a=[4,6,2,62,9,0]    
x=selection_sort(a)
print("After selection sort:",x)
