def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    array1p=0
    array2p=0
    diff=0
    smallestPair=[]
    small=float("inf")
    while array1p<len(arrayOne) and array2p<len(arrayTwo):
        firstNum=arrayOne[array1p]
        secondNum=arrayTwo[array2p]
        if firstNum<secondNum:
            diff=secondNum-firstNum
            array1p+=1
        elif secondNum<firstNum:
            diff=firstNum-secondNum
            array2p+=1
        else:
            return [firstNum,secondNum] 
        if small>diff:
            small=diff
            smallestPair=[firstNum,secondNum]
    return smallestPair
    
    # Write your code here.
     
