def check(arr):
    
    for i in range(len(arr)):
        if len(set(arr))==1:
            print("1st",arr[i])
            # pass
        
        elif i!=0 and i!=(len(arr)-1):
            
            
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                print("2nd",arr[i])
        else:
            if i==0:
                if arr[i]<arr[i+1]:
                    print("3rd",arr[i])
            else:
                if arr[i]>arr[i-1]:
                    print("3rd",arr[i])
                    
        
arr = [1,2,3,4,5,6,7,8]
check(arr)