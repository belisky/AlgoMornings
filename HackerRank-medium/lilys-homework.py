#O(nlogn)

def lilysHomework(arr):
    
    def no_of_swaps(arr):
        indexmap={}
        for i in range(len(arr)):
            indexmap[arr[i]]=i
        s_arr=sorted(arr)
        res=0
        for j in range(len(arr)):
            if arr[j]!=s_arr[j]:
                res+=1
                
                swap_ind=indexmap[s_arr[j]]
                indexmap[arr[j]]=swap_ind
                arr[j],arr[swap_ind]=arr[swap_ind],arr[j]
        return res
        
    nml=no_of_swaps(arr[::])
    rvr=no_of_swaps(arr[::-1])
    
    return min(nml,rvr) 
        
  