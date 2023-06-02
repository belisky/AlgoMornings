def minRewards(scores):
    minscore=[1 for _ in scores]
    for i in range(1,len(scores)):
        if scores[i]>scores[i-1]:
            minscore[i]=minscore[i-1]+1
    for i in reversed((range(len(scores)-1))):
        if scores[i]>scores[i+1]:
            minscore[i]=max(minscore[i],minscore[i+1]+1)
    return sum(minscore)
            
        
    # Write your code here.
# Solution 2
# def minRewards(scores):
#     rewards=[1 for _ in scores]
#     localMinIds=getLocalMinIds(scores)
#     for localMinId in localMinIds:
#         expandFromLocal(localMinId,scores,rewards)
#     return sum(rewards)

# def getLocalMinIds(array):
#     if len(array)==1:
#         return [0]
#     localMinIds=[]
#     for i in range(len(array)):
#         if i==0 and array[i]<array[i+1]:
#             localMinIds.append(i)
#         if i==len(array)-1 and array[i]<array[i-1]:
#             localMinIds.append(i)
#         if i==0 or i==len(array)-1:
#             continue
#         if array[i]<array[i+1] and array[i]<array[i-1]:
#             localMinIds.append(i)
#     return localMinIds

# def expandFromLocal(localMinId,scores,rewards):
#     leftId=localMinId-1
#     while leftId>=0 and scores[leftId]>scores[leftId+1]:
#         rewards[leftId]=max(rewards[leftId],rewards[leftId+1]+1)
#         leftId-=1
#     rightId=localMinId+1
#     while rightId<len(scores) and scores[rightId]>scores[rightId-1]:
#         rewards[rightId]=rewards[rightId-1]+1
#         rightId+=1
#     # Write your code here.
#     pass

