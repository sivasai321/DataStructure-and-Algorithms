def is_subsequence(arr1, arr2):
    i = 0
    j = 0
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] == arr2[j]:
            i += 1
        j += 1
    return i == len(arr1)


arr1 = [3,4,6]
arr2 = [2,3,4,6,9]
print(is_subsequence(arr1, arr2))