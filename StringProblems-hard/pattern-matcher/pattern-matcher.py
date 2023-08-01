def patternMatcher(pattern, string):
    if len(pattern)>len(string):
        return []
    newArrangement=getNewArrangement(pattern)
    switched=newArrangement[0]!=pattern[0]
    countChInPattern={'x':0,'y':0}
    firstYpos=getCountChInPatternAndFirstY(newArrangement,countChInPattern)
    if countChInPattern['y']!=0:
        for potX in range(1,len(string)):
            potY=(len(string)-potX*countChInPattern['x'])/countChInPattern['y']

            if potY<=0 or potY%1!=0:
                continue
            potY=int(potY)
            yIdx=firstYpos*potX
            x=string[:potX]
            y=string[yIdx:yIdx+potY]
            potMatch=map(lambda char:x if char=='x' else y,newArrangement)
            if string==''.join(potMatch):
                return [x,y] if not switched else [y,x]
    else:
        potX=len(string)/countChInPattern['x']
        if potX%1==0:
            potX=int(potX)
            x=string[:potX]
            potMatch=map(lambda char:x,newArrangement)
            if string==''.join(potMatch):
                return [x,''] if not switched else ['',x]
    return []
def getNewArrangement(pattern):
    patternChars=list(pattern)
    if patternChars[0]=='x':
        return patternChars
    else:
        return list(map(lambda char:'x' if char=='y' else 'y',patternChars))

def getCountChInPatternAndFirstY(pattern,counts):
    firstY=-1
    for i,char in enumerate(pattern):
        counts[char]+=1
        if char=='y' and firstY==-1:
            firstY=i
    return firstY
