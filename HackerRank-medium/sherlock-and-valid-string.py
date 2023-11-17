def isValid(s):
    cnt=Counter(s)
    if len(set(cnt.values()))==1:
        return 'YES'
    elif len(set(cnt.values()))>2:
        return 'NO'
    else:
        for k in cnt:
            cnt[k]-=1
            tmp=list(cnt.values())
            try:
                tmp.remove(0)
            except:
                pass
            if len(set(tmp))==1:
                return 'YES'
            else:
                cnt[k]+=1
        return 'NO'