def sortzero(a):
    index=0
    for i in range(0,len(a)):
        if a[i]!=0:
            a[index]=a[i]       
            index +=1

    for i in range(index,len(a)):
        a[i]=0   

    print(a)         


def linearSearch(a,srch):
    for i in range(0,len(a)):
        if a[i]==srch:
            print("element found at index:",i)
            return True
    return None        

list=[1,0,5,6,0,0,8,9,0]
# sortzero(list)
linearSearch(list,6)
