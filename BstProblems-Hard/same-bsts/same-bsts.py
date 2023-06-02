def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne)==0 and len(arrayTwo)==0:
        return True
    if arrayOne[0]!=arrayTwo[0]:
        return False
    leftOne=getLeftSubTree(arrayOne)
    leftTwo=getLeftSubTree(arrayTwo)
    rightOne=getRightSubTree(arrayOne)
    rightTwo=getRightSubTree(arrayTwo)
    cur=arrayOne

    return sameBsts(leftOne,leftTwo) and sameBsts(rightOne,rightTwo)

def getLeftSubTree(array):
    small=[]
    for i in range(1,len(array)):
        if array[i]<array[0]:
            small.append(array[i])
    return small
def getRightSubTree(array):
    big=[]
    for i in range(1,len(array)):
        if array[i]>=array[0]:
            big.append(array[i])
    return big
            
    
    # Write your code here.
 
