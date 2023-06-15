def minNumberOfCoinsForChange(n, denoms):
    numOfCoins=[float('inf') for amt in range(n+1)]
    numOfCoins[0]=0
    for denom in denoms:
        for amount in range(denom,len(numOfCoins)):
            numOfCoins[amount]=min(numOfCoins[amount],numOfCoins[amount-denom]+1)
    return numOfCoins[n] if numOfCoins[n]!=float('inf') else -1
    # Write your code here.
 
