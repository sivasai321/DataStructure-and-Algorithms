
# Sum  of N natural numbers

def sumnum(value):
    sum=value*(value+1)//2
    return sum
x=sumnum(5)
print(x)    

#Prime numbers

a=[3,5,1,2,52,65,22,12]
 
for i in range(0,len(a)):
    flag=0
    for j in range(2,a[i]//2):
        if a[i]%j==0:
            flag=1
            break

    if flag==0 and a[i]!=1:
        print(a[i])



#Fibonacci series
# def finonacci(n):
#     if n<=1:
#         return n
#     else:
#         return finonacci(n-1)+finonacci(n-2) 


# x=finonacci(10)
# print(x)           


