def largestRange(array):
    nums=set(array)
    maxL=0
    best=[]
    for num in array:
        if num-1 not in nums:
            i=num
            while i in nums:
                i+=1
            curL=i-num
            if curL>maxL:
                maxL=curL
                best=[num,i-1]
    return best
    # Write your code here.
    pass



# Solution 2
# def largestRange(array):
#     integers={}
#     longestRange=[]
#     longestSize=0
#     for i in array:
#         integers[i]=True
#     for i in integers:
#         if not integers[i]:
#             continue
#         left=i-1
#         count=1
#         while left in integers:
#             count+=1
#             integers[left]=False
#             left-=1
#         right=i+1
         
#         while right in integers:
#             count+=1
#             integers[right]=False
#             right+=1
      
#         if count>longestSize:
#             longestSize=count
#             longestRange=[left+1,right-1]
#     return longestRange
    
#     # Write your code here.
#     pass
