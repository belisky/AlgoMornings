def zeroSumSubarray(nums):
    curSum=0
    sumsDict=set([0])     
    for num in nums:
        curSum+=num
        if curSum in sumsDict:
            return True
        
        sumsDict.add(curSum)
    
    # Write your code here.
    return False
