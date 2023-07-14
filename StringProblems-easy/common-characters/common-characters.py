def commonCharacters(strings):
    smallestString=getSmallestString(strings)
    potentialCommonCharacters=set(smallestString)

    for string in strings:
        removeNonexistentCharacters(string,potentialCommonCharacters)

    return list(potentialCommonCharacters)

def getSmallestString(strings):
    smallestString=strings[0]
    for string in strings:
        if len(string)<len(smallestString):
              smallestString=string
    return smallestString

def removeNonexistentCharacters(string,potentialCommonCharacters):
    uniqueStringChars=set(string)
    for char in list(potentialCommonCharacters):
        if char not in uniqueStringChars:
            potentialCommonCharacters.remove(char)
                                
  



#Solution 2
#O(nm)-time and O(c)-space where c is the length of the longest uniqueCharset.
# def commonCharacters(strings):
#     characterCounts={}
#     for string in strings:
#         uniqueCharSet=set(string)
#         for char in uniqueCharSet:
#             if char not in characterCounts:
#                 characterCounts[char]=0
#             characterCounts[char]+=1
#     finalChars=[]
#     for char,count in characterCounts.items():
#         if count==len(strings):
#             finalChars.append(char)
#     # Write your code here.
#     return finalChars
