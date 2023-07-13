def runLengthEncoding(string):
    encodedChars=[]
    curRunLength=1

    for i in range(1,len(string)):
        curChar=string[i]
        prevChar=string[i-1]
        if (curChar!=prevChar or curRunLength==9):
            encodedChars.append(str(curRunLength))
            encodedChars.append(prevChar)
            curRunLength=0
        curRunLength+=1

        
    encodedChars.append(str(curRunLength))
    encodedChars.append(string[-1])
    return ''.join(encodedChars)
    
    # Write your code here.
    
