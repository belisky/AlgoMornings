def longestSubstringWithoutDuplication(string):
    start=0
    letterPosition={}
    longestSub=[0,1]
    for i in range(len(string)):
        if string[i] in letterPosition:
            start=max(start,letterPosition[string[i]]+1)
        if longestSub[1]-longestSub[0]<i+1-start:
            longestSub=[start,i+1]           
        letterPosition[string[i]]=i
    return string[longestSub[0]:longestSub[1]]
 
# print(longestSubstringWithoutDuplication(string='nobelisyourdevopsguy'))