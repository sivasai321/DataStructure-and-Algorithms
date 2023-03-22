def find_numbers(nums):
    eve_count=0
    for num in nums:
        count =0
        n=num
        while n>0:
            count +=1
            n=n/10
            
        if count %2 ==0:
            eve_count+=1
    return eve_count

arr=[12,1235655,1234,123]
print(find_numbers(arr))
# print("big">"small")