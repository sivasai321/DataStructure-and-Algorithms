def merge_sorted_arrays(arr1,arr2):
    # merg = arr1+arr2
    # merg.sort()
    
    merge=[]
    n=len(arr1)-1
    m=len(arr2)-1
    for i in range((n+m)+2):
        if i<=n:
            merge.insert(i, arr1[i])
        else:
            merge.insert(i, arr2[i-(n+1)])
    merge.sort()
    
    return merge

arr1=[1,5,10,24,67]
arr2=[4,7,8,9,0]
print(merge_sorted_arrays(arr1, arr2))