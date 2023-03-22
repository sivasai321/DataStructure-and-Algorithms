def heap_sort(arr):
    n=len(arr)
    for i in range(n//2 - 1, - 1, - 1):
        max_heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        max_heapify(arr,i,0)
        
        
def max_heapify(arr, n ,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left]>arr[largest]:
        largest = left
    if right < n and arr[right]>arr[largest]:
        largest = right
    
    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,n,largest)
        
arr = [12,34,2,45,12,67,99,43]
heap_sort(arr)
print(arr)