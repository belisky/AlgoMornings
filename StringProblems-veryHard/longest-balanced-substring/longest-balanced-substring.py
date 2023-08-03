def longestBalancedSubstring(string):
    maxL=0
    openingCount=0
    closingCount=0

    for char in string:
        if char=='(':
            openingCount+=1
        else:
            closingCount+=1

        if openingCount==closingCount:
            maxL=max(maxL,closingCount*2)
        elif closingCount>openingCount:
            openingCount,closingCount=0,0
    openingCount,closingCount=0,0
   
    for i in reversed(range(len(string))):
        char=string[i]
        if char=='(':
            openingCount+=1
        else:
            closingCount+=1

        if openingCount==closingCount:
            maxL=max(maxL,openingCount*2)
        elif closingCount<openingCount:
            openingCount,closingCount=0,0
     
    return maxL


# O(n) time O(n) space
# def longestBalancedSubstring(string):
#     maxL=0
#     indexStack=[]
#     indexStack.append(-1)

#     for i in range(len(string)):
#         if string[i]=='(':
#             indexStack.append(i)
#         else:
#             indexStack.pop()
#             if len(indexStack)==0:
#                 indexStack.append(i)
#             else:
#                 balancedStringStart=indexStack[len(indexStack)-1]
#                 cur=i-balancedStringStart
#                 maxL=max(maxL,cur)
#     return maxL
 
