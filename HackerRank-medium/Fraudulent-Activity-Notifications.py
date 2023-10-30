#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def getMedian(countFreq,d,mid):
    counter=0
    pos=0
    while counter<mid:
        counter+=countFreq[pos]
        pos+=1
    pos-=1
    if counter>mid or d%2!=0:
        return pos
    else:
        return (2*pos+1)/2

def activityNotifications(expenditure, d):
    countFreq=[0]*201
    end=d
    for i in range(end):
        countFreq[expenditure[i]]+=1
    notif=0
    if d%2==0:
        mid=int(d/2)
    else:
        mid=int(d/2)+1
    length=len(expenditure)
    cur=0
    while end<length:
        median=getMedian(countFreq,d,mid)
        if expenditure[end]>=2*median:
            notif+=1
        countFreq[expenditure[cur]]-=1
        countFreq[expenditure[end]]+=1
        cur+=1
        end+=1
    return notif
    # Write your code here
