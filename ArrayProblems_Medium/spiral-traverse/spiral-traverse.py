def spiralTraverse(array):
    sr,er=0,len(array)-1
    sc,ec=0,len(array[0])-1
    arr=[] 
   
    while sr<=er and sc<=ec:
        for top in range(sc,ec+1):
            arr.append(array[sr][top])  
         
        for right in range(sr+1,er+1):             
            arr.append(array[right][ec]) 
        for bottom in reversed(range(sc,ec)):
            if sr==er:
                break
            arr.append(array[er][bottom])
 
        for left in reversed(range(sr+1,er)): 
            if sc==ec:
                break           
            arr.append(array[left][sc])
        # print(arr)
        sr+=1
        er-=1
        sc+=1
        ec-=1
       
  
    return arr
        
    # Write your code here.
  
