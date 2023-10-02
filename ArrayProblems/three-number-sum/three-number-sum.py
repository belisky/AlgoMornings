def threeNumberSum(array, targetSum):
    array.sort()
    res=[]
   
    for i in range(len(array)-2):        
        left=i+1
        right=len(array)-1
        while left<right:
            if targetSum<array[left]+array[right]+array[i]:
                right-=1
            elif targetSum>array[left]+array[right]+array[i]:            
                left+=1 
            else:
                res.append([array[i],array[left],array[right]])
                right-=1
                left+=1
    return res