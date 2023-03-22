def b_sort(a):
    for i in range(len(a)-1):
        swapped=False
        print(i,'from i loop')
        for j in range(len(a)-1-i):
            print(j,'from j loop')
            if a[j]>a[j+1]:
                [a[j],a[j+1]]=[a[j+1],a[j]]
                swapped=True
        if swapped==False:
            break
            





a=[3,5,1,32,56,2,23,4]
b_sort(a)
print(a)