def binar(a,x,low,high):
    while low < high:
        mid=low+high//2
        if a[mid]==x:
            return mid
        elif x<a[mid]:
            return binar(a,x,0,mid+1) 
        else:
            return binar(a,x,low,mid-1)   

    return -1         

a=[1,2,3,4,5,6,7,8,9]
x=3
res=binar(a,x,0,len(a))
if res==-1:
    print("Element not found")

else:
    print("element found at",res)