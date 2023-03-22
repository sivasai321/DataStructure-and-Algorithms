def consecuitive_ones(arr):
    n=len(arr)
    count=0
    result =0
    for i in range(0,n):
        if arr[i]!=1:
            count = 0
        else:
            count+=1
            result = max(result,count)
    return result
        
    
arr= [1,1,0,1,1,1]
print(consecuitive_ones(arr))