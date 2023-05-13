def firstDuplicateValue(array):
    # Write your code here.
    
    max_count = {}
    for _ , value in enumerate(array):
        if value  in max_count:
            max_count[value] += 1
            return value 
        else:
            max_count[value] = 1
            
    return -1
# Solution 2
# def firstDuplicateValue(array):
#     for value in array:
#         absVal=abs(value)
#         if array[absVal-1]<0:
#             return absVal
#         array[absVal-1]*=-1
#     return -1