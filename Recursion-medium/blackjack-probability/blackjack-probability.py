def blackjackProbability(target, startingHand):
    memo = {}
    return round(calculateProbability(startingHand, target, memo), 3)


def calculateProbability(currentHand, target, memo):
    if currentHand in memo:
        return memo[currentHand]
    if currentHand > target:
        return 1
    if currentHand+4 >= target:
        return 0

    totalProbability = 0
    for drawnCard in range(1, 11):
        totalProbability += 0.1 * \
            calculateProbability(currentHand+drawnCard, target, memo)
    memo[currentHand] = totalProbability
    return totalProbability
