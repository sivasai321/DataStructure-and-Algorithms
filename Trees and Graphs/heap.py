def heapify(arr):

    def min_heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[largest]:
            largest = left
        if right < n and arr[right] < arr[largest]: 
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            min_heapify(arr, n, largest)
    n = len(arr)
    i = n // 2 - 1

   
    for num in range(i, -1, -1):
        min_heapify(arr, n, num)
    return arr
arr = [12,45,23,65,87,98,9]
heapify(arr)
print(arr)