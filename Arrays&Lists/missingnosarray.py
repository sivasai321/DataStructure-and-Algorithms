
def missing_numbers(arr):
    n = len(arr)
    full_set = set(range(1, n + 1))
    array_set = set(arr)
    missing_numbers = list(full_set - array_set)
    return missing_numbers

arr = [6, 1, 3, 4, 8, 7]
miss = missing_numbers(arr)
print("The missing numbers are", miss)


 