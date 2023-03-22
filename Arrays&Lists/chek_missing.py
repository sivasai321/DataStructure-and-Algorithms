def check_missing(arr,n):
    print(arr)
    for i in range(1,n):
        if i not in arr:
            print(i)
        
            
arr = [1,3,6,2,4]
check_missing(arr,6 )
    