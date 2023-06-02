def moveElementToEnd(array, toMove):
    print(array)
    i=0
    secondp=len(array)-1
    while i<secondp:
        if array[i]==toMove:
            array[secondp],array[i]=array[i],array[secondp]
            secondp-=1
        else:
            i+=1 
 
    return array
 
