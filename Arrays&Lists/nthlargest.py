# a=[]
# n=int(input("enter limit"))
# for i in range(0,n):
#     b=int(input("enter elements "+str(i)+":"))
#     a.append(b)

# for i in range(0,len(a)):
#     for j in range(0,len(a)-i-1):
#         if a[j]>a[j+1]:
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp

# print(a)  
# x=int(input("Enter nth value"))  
# print("nth largest number:",a[n-x])        


# listy=[1,2,4,1,24,5,6,78,9,34,24]
# unique=[]
# dupli=[]
# for i in listy:
#     if i not in unique:
#         unique.append(i)

#     elif i not in dupli:
#         dupli.append(i)   

# print(unique)         
# print(dupli)

# def fibo(n):
#     if n<=1:
#         return n
#     else :
#         return fibo(n-1)+fibo(n-2)    

# n=10

# for i in range(0,n) :
#     print(fibo(i))
      

# def missingnos(a,n):
#     fullset=set(range(1,n+1))
#     array_set=set(a)
#     missnos=list(fullset-array_set)
#     return missnos

# arr=[1,2,3,6,8,11]
# m=missingnos(arr,16)
# print(m)