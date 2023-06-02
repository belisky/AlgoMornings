def missingNumbers(nums):
    total=sum(range(1,len(nums)+3))
    for num in nums:
        total-=num
    averageMissingValue=total//2
    foundFirstHalf=0
    foundSecondHalf=0
    for num in nums:
        if num<=averageMissingValue:
            foundFirstHalf+=num
        else:
            foundSecondHalf+=num
    expectedFirstHalf=sum(range(1,averageMissingValue+1))
    expectedSecondHalf=sum(range(averageMissingValue+1,len(nums)+3))
    return [expectedFirstHalf-foundFirstHalf,expectedSecondHalf-foundSecondHalf]

# # Solution2. O(n) time, O(n) space complexity
# def missingNumbers(nums):
#     availableNums=set(nums)
#     solution=[]
#     for num in nums:
#         if num not in availableNums:
#             solution.append(num)
#     return solution

  
   
