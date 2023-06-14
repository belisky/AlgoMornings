def numberOfWaysToMakeChange(n, denoms):
    ways=[0 for _ in range(n+1)]
    ways[0]=1
    for coin_denomination in denoms:
        for target_amount in range(1,n+1): 
            # if the amount>coin_denomination, that means that particular coin can be used in making a change for that amount.
            if  target_amount>=coin_denomination:
                ways[target_amount]+=ways[target_amount-coin_denomination]
    return ways[n]
    # Write your code here.
 
