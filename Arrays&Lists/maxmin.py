def maxmin(a):
   max=0
   min=a[0]
   for i in range (len(arr)):
        if a[i]>=max:
            max=a[i]
        elif a[i]<=min:
            min=a[i]    
   print("Max",max)
   print("Min",min)

def targetsum(a,target):
    for i in range(len(a)-1):
        for j in range (len(a)):
           if a[i]+a[j]==target:
            return a[i],a[j]

    return None

def remove_sorted_duplicates(a):
    count=1
    for i in range(len(a)-1):
            if(a[i]!=a[i+1]):
                a[count]=a[i+1]
                count +=1
                
                
    return (a[:count]) 

ar=[3,2,4]
arr=[132,2,13,145,6,1,8,9,22]
arr2=[1,1,2,3,4,5,5,6,7,7,8]
maxmin(arr)

r=targetsum(ar,6)
print(r)
print(arr2)
x=remove_sorted_duplicates(arr2)
print(x)