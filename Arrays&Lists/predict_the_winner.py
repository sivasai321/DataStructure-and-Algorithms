def PredictTheWinner(nums):
        p1=0
        p2=0
        for i in range(0,len(nums)):
            if i%2==0:
                p1+=nums[i]
            else:
                p2+=nums[i]
        
        if p1>p2 or p1==p2:
            return True
        else:
            return False
        
print(PredictTheWinner([1,2]))