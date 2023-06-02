def longestPeak(array):
    count=1
    lpeak=0
    i=1
    j=0
    k=0
    while i<len(array)-1:
        if  array[i]>array[i+1] and array[i-1]<array[i]:
            j=i
            while j>0 and array[j]>array[j-1]:              
                j-=1
            k=i
            while k<len(array)-1 and array[k]>array[k+1]:              
                k+=1
                i=k
        i+=1
        if k-j>lpeak:
            lpeak=k-j+1
            
    return lpeak
            
        
    # Write your code here.
    
