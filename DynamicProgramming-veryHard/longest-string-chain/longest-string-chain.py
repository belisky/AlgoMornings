def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextStr": "", "maxChainLen": 1}
    sortedStrings = sorted(strings, key=len)
    for string in sortedStrings:
        findLongestStrChain(string, stringChains)
    return buildLongestStringChain(strings, stringChains)


def findLongestStrChain(string, stringChains):
    for i in range(len(string)):
        smallerString = string[0:i]+string[i+1:]
        if smallerString not in stringChains:
            continue
        tryUpdateLongestStrChain(string, smallerString, stringChains)


def tryUpdateLongestStrChain(curString, smallerString, stringChains):
    smallerStrChainLen = stringChains[smallerString]["maxChainLen"]
    curStringChainLen = stringChains[curString]["maxChainLen"]
    if smallerStrChainLen+1 > curStringChainLen:
        stringChains[curString]['maxChainLen'] = smallerStrChainLen+1
        stringChains[curString]['nextStr'] = smallerString
        # Write your code here.


def buildLongestStringChain(strings, stringChains):
    maxChainLen = 0
    chainStartStr = ""
    for str in strings:
        if stringChains[str]['maxChainLen'] > maxChainLen:
            maxChainLen = stringChains[str]['maxChainLen']
            chainStartStr = str
    strChains = []
    curStr = chainStartStr
    while curStr != '':
        strChains.append(curStr)
        curStr = stringChains[curStr]['nextStr']
    return [] if len(strChains) == 1 else strChains
