def firstNonRepeatingCharacter(string):
    char_frequency={}
    for i in string:
        if i not in char_frequency:
            char_frequency[i]=0

        char_frequency[i]+=1
    for i in char_frequency:
        if char_frequency[i]<2:
            return string.index(i)
 
    return -1
