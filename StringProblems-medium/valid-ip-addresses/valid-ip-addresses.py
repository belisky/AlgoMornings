def validIPAddresses(string): 
    validIps=[]

    for i in range(1,min(len(string),4)):
        curIpAddr=["","","",""]
        curIpAddr[0]=string[:i]
        if not isValidPart(curIpAddr[0]):
            continue

        for j in range(i+1,i+min(len(string)-i,4)):
            curIpAddr[1]=string[i:j]
            if not isValidPart(curIpAddr[1]):
                continue

            for k in range(j+1,j+min(len(string)-j,4)):
                curIpAddr[2]=string[j:k]
                curIpAddr[3]=string[k:]

                if isValidPart(curIpAddr[2]) and isValidPart(curIpAddr[3]):
                     
                    validIps.append('.'.join(curIpAddr))
    # Write your code here.
    return validIps

def isValidPart(string):
    strAsInt=int(string)
    if strAsInt>255:
        return False
    return len(string)==len(str(strAsInt))
