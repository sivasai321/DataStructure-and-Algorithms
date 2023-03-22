def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=a[:mid]
    right=a[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

def merge(left,right):
    rst=[]
    i=0
    j=0
    while i< len(left) and j<len(right):
        if left[i]<right[j]:
            rst.append(left[i])
            i+=1
        else:
            rst.append(right[j]) 
            j+=1
    rst+=left[i:]        
    rst+=right[j:]
    return rst

a=[3,1,3444,123,423,53,524]

r=merge_sort(a)
print(r)
