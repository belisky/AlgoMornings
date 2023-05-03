def fourNumberSum(array, targetSum):
    initSums={}
    quad=[]
    for i in range(1,len(array)-1):
        for j in range(i+1,len(array)):
            curSum=array[i]+array[j]
            diff=targetSum-curSum
            if diff in initSums:
                for duo in initSums[diff]:
                    quad.append([*duo,array[i],array[j]])
        for k in range(0,i):
            curSum=array[i]+array[k]
            if curSum not in initSums:
                initSums[curSum]=[[array[i],array[k]]]
            else:
                initSums[curSum].append([array[i],array[k]])
    return quad
     
   
