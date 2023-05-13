def isMonotonic(array):
    inc=0
    dec=0
    for i in range(len(array)-1):
        if array[i+1]>array[i]:
            inc+=1
        elif array[i+1]<array[i]:   
            dec+=1
 
    return False if inc>0 and dec>0 else True
 
        
    
     
    # Write your code here.
     
