def longestPalindromicSubstring(string):
    curLongest=[0,1]
    for i in range(1,len(string)):
        odd=getLongestPalindromic(string,i-1,i+1)
        even=getLongestPalindromic(string,i-1,i)
        longest=max(even,odd,key=lambda x: x[1] - x[0])
        curLongest=max(longest,curLongest,key=lambda x: x[1] - x[0])
    return string[curLongest[0] : curLongest[1]]
        

def getLongestPalindromic(string,startIdx,endIdx):
    while startIdx>=0 and endIdx<len(string):
        if string[startIdx]!=string[endIdx]:
            break

        startIdx-=1
        endIdx+=1
    return [startIdx+1,endIdx]
    # Write your code here.
 