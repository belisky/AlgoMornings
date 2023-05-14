def subarraySort(array):
    minOutOfPlace=float('inf')
    maxOutOfPlace=float('-inf')
    
    for i in range(len(array)):
        num=array[i]
        if isOutOfPlace(i,num,array):
            minOutOfPlace=min(minOutOfPlace,num)
            maxOutOfPlace=max(maxOutOfPlace,num)
            
    if minOutOfPlace==float('inf') and maxOutOfPlace==float('-inf'):
        return [-1,-1]
        
    startOfUnsort=0
    
    while minOutOfPlace>=array[startOfUnsort]:
        startOfUnsort+=1
        
    endOfUnsort=len(array)-1
    
    while maxOutOfPlace <=array[endOfUnsort]:
        endOfUnsort-=1
    return [startOfUnsort,endOfUnsort]


def isOutOfPlace(i,num,array):
    if i==0:
        return num>array[i+1]
    if i==len(array)-1:
        return num<array[i-1]
    return num>array[i+1] or num<array[i-1]
        # Write your code here.
    pass
