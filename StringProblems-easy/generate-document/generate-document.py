def generateDocument(characters, document):
    charCount={}
    for i in characters:
        if i not in charCount:
            charCount[i]=0

        charCount[i]+=1
    for i in document:
        if i not in charCount or charCount[i]<1:
            return False
        charCount[i]-=1
    return True
    
    # Write your code here.
     
