def smallestSubstringContaining(bigString, smallString):
    smallStringFrequency=getCharCounts(smallString)
    subBounds=getStringBounds(smallStringFrequency,bigString)
    charString=getStringFromBounds(bigString,subBounds)
    return charString
    # Write your code here.
  
def getStringBounds(target,string):
    subStringBounds=[0,float('inf')]
    subStringChar={}
    numUnique=len(target.keys())
    numUniqueDone=0
    leftIdx=0
    rightIdx=0
    while rightIdx<len(string):
        rightCh=string[rightIdx]
        if rightCh not in target:
            rightIdx+=1
            continue
        increaseCharCount(rightCh,subStringChar)
        if subStringChar[rightCh]==target[rightCh]:
            numUniqueDone+=1
        while numUniqueDone==numUnique and leftIdx<=rightIdx:
            subStringBounds=getCloseBounds(leftIdx,rightIdx,subStringBounds[0],subStringBounds[1])
            leftCh=string[leftIdx]
            if leftCh not in target:
                leftIdx+=1
                continue
            if subStringChar[leftCh]==target[leftCh]:
                numUniqueDone-=1
            decreaseCharCount(leftCh,subStringChar)
            leftIdx+=1
        rightIdx+=1
    return subStringBounds

def getCloseBounds(l,r,subL,subR):
    if r-l<subR-subL:
        return [l,r]
    else:
        return [subL,subR]
def getStringFromBounds(string,bounds):
    start,end=bounds
    if end==float('inf'):
        return ''
    return string[start:end+1]
    
def getCharCounts(string):
    charCounts={}
    for i in string:
        increaseCharCount(i,charCounts)
    return charCounts

def increaseCharCount(char,charCounts):
    if char not in charCounts:
        charCounts[char]=0

    charCounts[char]+=1
    
def decreaseCharCount(char,charCounts):
    charCounts[char]-=1
        
