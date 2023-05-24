def bestSeat(seats):
    bestSeat=-1
    maxSpace=0
    leftPointer=0
    while leftPointer<len(seats):
        rightPointer=leftPointer+1
        while rightPointer<len(seats) and seats[rightPointer]==0:
            rightPointer+=1
        availableSpace=rightPointer-leftPointer-1
        if availableSpace>maxSpace:
            bestSeat=(leftPointer+rightPointer)//2
            maxSpace=availableSpace
        leftPointer=rightPointer
    return bestSeat
    # Write your code here.
  
