def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maxA = [array[0]]
    maxAMinusB = [float('-inf')]
    maxAMinusBPlusC = [float('-inf')]*2
    maxAMinusBPlusCMinusD = [float('-inf')]*3

    for idx in range(1, len(array)):
        curMax = max(maxA[idx-1], array[idx])
        maxA.append(curMax)
    for idx in range(1, len(array)):
        curMax = max(maxAMinusB[idx-1], maxA[idx-1]-array[idx])
        maxAMinusB.append(curMax)
    for idx in range(2, len(array)):
        curMax = max(maxAMinusBPlusC[idx-1], maxAMinusB[idx-1]+array[idx])
        maxAMinusBPlusC.append(curMax)
    for idx in range(3, len(array)):
        curMax = max(maxAMinusBPlusCMinusD[idx-1],
                     maxAMinusBPlusC[idx-1]-array[idx])
        maxAMinusBPlusCMinusD.append(curMax)
    # Write your code here.
    return maxAMinusBPlusCMinusD[len(maxAMinusBPlusCMinusD)-1]
