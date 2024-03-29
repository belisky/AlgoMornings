def numbersInPi(pi, numbers):
    numbsTab={number:True for number in numbers}
    minSpaces=getMinSpaces(pi,numbsTab,{},0)
    return -1 if minSpaces==float('inf') else minSpaces
    # Write your code here.

def getMinSpaces(pi,numbersTable,cache,idx):
    if idx==len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces=float('inf') 
    for i in range(idx,len(pi)):
        prefix=pi[idx:i+1]
        if prefix in numbersTable:
            minSpacesInSuffix=getMinSpaces(pi,numbersTable,cache,i+1)
            minSpaces=min(minSpaces,minSpacesInSuffix+1)
    cache[idx]=minSpaces
    return cache[idx]
