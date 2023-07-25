def reverseWordsInString(string):
    words=[]
    start=0
    if string=='':
        return ''
        
    for i in range(len(string)):
        char=string[i]
        if char==" ":
            words.append(string[start:i])
            start=i+1
        
    words.append(string[start:i+1])
  
     
    return ' '.join(words[::-1])
