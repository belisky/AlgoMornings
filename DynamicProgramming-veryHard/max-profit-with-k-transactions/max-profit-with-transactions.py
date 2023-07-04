def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0

    profits = [[0 for d in prices] for t in range(k+1)]
    for t in range(1, k+1):
        maxSoFar = float('-inf')
        for d in range(1, len(prices)):
            maxSoFar = max(maxSoFar, profits[t-1][d-1]-prices[d-1])
            profits[t][d] = max(profits[t][d-1], maxSoFar+prices[d])
    return profits[-1][-1]


# O(nk) time and O(n) space.
# def maxProfitWithKTransactions(prices, k):
#     if not len(prices):
#         return 0
#     evenProfits=[0 for d in prices]
#     oddProfits=[0 for d in prices]
#     for t in range(1,k+1):
#         maxSoFar=float('-inf')
#         if t%2==1:
#             curProfits=oddProfits
#             prevProfits=evenProfits
#         else:
#             prevProfits=oddProfits
#             curProfits=evenProfits
#         for d in range(1,len(prices)):
#             maxSoFar=max(maxSoFar,prevProfits[d-1]-prices[d-1])
#             curProfits[d]=max(curProfits[d-1],maxSoFar+prices[d])
#     return curProfits[-1]
#     # Write your code here.-1
#     pass
