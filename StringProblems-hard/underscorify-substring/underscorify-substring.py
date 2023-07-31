def underscorifySubstring(string, substring):
    idx_open=-1
    idx_close=-1
    start=0
    idx=0
    under=''
    while idx<=len(string)-len(substring):
        cur=string[idx:idx+len(substring)]
        if cur==substring:
            if idx_open<0:
                under+='_'
                idx_open=idx
            idx_close=idx+len(substring)
            
        elif idx==idx_close:
            under+='_'
            idx_open=-1
            idx_close=-1
        under+=string[idx]        
        idx+=1
    if idx_close>0:
        while idx<idx_close:
            under+=string[idx]
            idx+=1
        under+='_'
    under+=string[idx:]
            
    return under        
    # Write your code here.



#Solution 2
# def underscorifySubstring(string, substring):
#     locations=collapse(getLocations(string,substring))
#     return underscore(string,locations)

# def getLocations(string,substring):
#     locations=[]
#     start=0
#     while start<len(string):
#         pos=string.find(substring,start)
#         if pos!=-1:
#             locations.append([pos,pos+len(substring)])
#             start=pos+1
#         else:
#             break
#     return locations

# def collapse(locations):
#     if not len(locations):
#         return locations
#     newLoc=[locations[0]]
#     prev=newLoc[0]
#     for i in range(1,len(locations)):
#         cur=locations[i]
#         if cur[0]<=prev[1]:
#             prev[1]=cur[1]
#         else:
#             newLoc.append(cur)
#             prev=cur
#     return newLoc

# def underscore(string,locations):
#     underscoredString=[]
#     isInMiddle=False
#     start=0
#     locCounter=0
#     one_or_two=0
#     while locCounter<len(locations) and start<len(string):
#         if  start==locations[locCounter][one_or_two]:
#             underscoredString.append('_')
#             isInMiddle=not isInMiddle            
#             if not isInMiddle:
#                 locCounter+=1
#             one_or_two=0 if one_or_two==1 else 1
#         underscoredString.append(string[start])
#         start+=1
#     if locCounter<len(locations):
#         underscoredString.append('_')
#     elif start<len(string):
#         underscoredString.append(string[start:])
#     return ''.join(underscoredString)
#     # Write your code here.
    

   
