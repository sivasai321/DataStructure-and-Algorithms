def bigger(str):
    list =[]
    list[:0]=str
    largest = list[0]
    position =0
    for i in range(1,len(list)):
        if ord(list[i])>ord(largest):
            largest = list[i]
            position = i
    
    if position ==0 :
        largest = list[1]
        position = 0
        for i in range(1,len(list)):
            if ord(list[i])>ord(largest):
                largest = list[i]
                position = i
    temp = list[position]
    list[position] = list[position-1]
    list[position-1] = temp
    print(list)    
    
str="ZBLAHBLAH"
bigger(str)    
    
