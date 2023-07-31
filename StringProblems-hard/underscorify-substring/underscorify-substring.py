def underscorifySubstring(string, substring):
    idx_open=-1
    idx_close=-1
    start=0
    idx=0
    under=''
    while idx<=len(string)-len(substring):
        cur=string[idx:idx+len(substring)]
        if cur==substring:
            if idx_open<0:
                under+='_'
                idx_open=idx
            idx_close=idx+len(substring)
            
        elif idx==idx_close:
            under+='_'
            idx_open=-1
            idx_close=-1
        under+=string[idx]        
        idx+=1
    if idx_close>0:
        while idx<idx_close:
            under+=string[idx]
            idx+=1
        under+='_'
    under+=string[idx:]
            
    return under        
    # Write your code here.
   
