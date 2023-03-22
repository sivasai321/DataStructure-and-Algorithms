def check(arr,extra):
    res =[]
    max_value= max(arr)
    for i in range(len(arr)):
        x= arr[i]+extra
        if x>=max_value:
            res.append(True)
        else:
            res.append(False)
            
    return res

arr = [2,3,5,1,3]
extra = 3
result = check(arr,extra)
print(result)
        