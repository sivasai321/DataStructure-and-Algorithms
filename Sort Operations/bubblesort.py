def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

    return a            


a=[3,5,1,32,56,2,23,4]
x=bubble_sort(a)
print(x)