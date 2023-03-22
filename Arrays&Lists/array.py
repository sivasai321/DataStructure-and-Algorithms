def binarySrch(a,x,low,high):
	mid=low+high//2
	if(a[mid]==x):
		return mid
	elif a[mid]<x:
		return binarySrch(a,x,0,mid+1)
	else:
		return binarySrch(a,x,mid,high)

   

list=[1,2,3,4,5,6,7,8,9]
x=4
r=binarySrch(list,x,0,len(list))
print(r)
