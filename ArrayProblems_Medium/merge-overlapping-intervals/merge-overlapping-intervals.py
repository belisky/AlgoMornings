def mergeOverlappingIntervals(intervals):
    sortedInt=sorted(intervals,key=lambda x:x[0])
    res=[]
    cur=sortedInt[0]
    res.append(cur)
    for i in sortedInt:
        curS,curE=cur
        nextS,nextE=i
        if curE>=nextS:
            cur[1]=max(curE,nextE)
        
        else:
            cur=i
            res.append(cur)
     
    return res
 
 
            
        
    
    # Write your code here.
  
