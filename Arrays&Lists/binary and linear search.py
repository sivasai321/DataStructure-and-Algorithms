def binary_search(arr,x,low,high):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            
            return binary_search(arr,x,0,mid+1)
        else:
           
            return binary_search(arr,x,low,mid-1)
    return -1
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 4
result = binary_search(arr, x,0,len(arr))
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")    


#Linear Search
# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1

# arr = [1,2,3,4,5,6,7,8,9]
# x = 5

# result = linear_search(arr, x)
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in the array")


