def remove_element(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            for j in range(i, len(arr)-1):
                arr[j] = arr[j+1]
            arr[len(arr)-1] = None
            break
    return arr[:len(arr)-1]

my_list = [1, 2, 3, 4,2,5]
my_list = remove_element(my_list, 2)
print(my_list) 