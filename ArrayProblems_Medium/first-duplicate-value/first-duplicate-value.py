def firstDuplicateValue(array):
    for value in array:
        absoluteValue=abs(value)
        if array[absoluteValue-1]<0:
            return absoluteValue
        array[absoluteValue-1]*=-1
    return -1
     

# Solution 2
# def firstDuplicateValue(array):
#     max_count = {}
#     for _ , value in enumerate(array):
#         if value  in max_count:
#             max_count[value] += 1
#             return value 
#         else:
#             max_count[value] = 1
            
#     return -1

