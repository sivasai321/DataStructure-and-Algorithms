def next_one(arr):
    n=len(arr)
    if arr[n-1] == 9:  
        for i in range(n,0,-1):
            if arr[i-1] == 9:
                arr[i-1]=0
                if arr[i-2]!= 9:
                    arr[i-2]=arr[i-2]+1  
                    break
    else:
        arr[n-1]+=1  
    print(arr)
  
next_one([3,9,9,4,9,9,9,9])