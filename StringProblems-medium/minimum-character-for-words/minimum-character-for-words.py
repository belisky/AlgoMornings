def minimumCharactersForWords(words):
    maxFrequencies={}
    chars=[]
    for word in words:
        charFreqInWord=countCharFreq(word)
        updateMaxFreq(charFreqInWord,maxFrequencies)
 
    for i in maxFrequencies:
        for j in range(maxFrequencies[i]):
            chars.append(i)
    return chars


def countCharFreq(string):
    charFreq={}
    for i in string:
        if i not in charFreq:
            charFreq[i]=0

        charFreq[i]+=1
    return charFreq
def updateMaxFreq(curWord,maxFreq):
    for i in curWord:
        if i not in maxFreq:
            maxFreq[i]=curWord[i]
        else:
            maxFreq[i]=max(maxFreq[i],curWord[i])
        

    
    # Write your code here.
 
