

def duplicate(arr):
    index = 1
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            arr[index] = arr[i+1]
            index+=1
            
    return arr,index

arr=[1,2,2,2,3,4,4,5]            
arr,index = duplicate(arr)
for i in range(index):
    print(arr[i])

        