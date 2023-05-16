def apartmentHunting(blocks, reqs):
    minReq=[dict() for _ in range(len(blocks))]
    for block in range(len(blocks)):
        for req in (reqs):
            minReq[block][req]=float('inf')
            if blocks[block][req]:
                minReq[block][req]=0
            elif block>0:
                minReq[block][req]=minReq[block-1][req]+1
 
 
    for block in range(len(blocks)-1,-1,-1):
        for req in reqs:
            if blocks[block][req]:
                minReq[block][req]=0
            
            elif block<len(blocks)-1:
                minReq[block][req]=min(minReq[block+1][req]+1,minReq[block][req])
                
    res=[0,max(minReq[0].values())]
    for i in range(1,len(blocks)):
        maxPerBlock=max(minReq[i].values())      
    
        if res[1]>maxPerBlock:            
            res[0]=i
            res[1]=maxPerBlock
    return res[0]
 
  
