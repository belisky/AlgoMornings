def twoNumberSum(array,target):
    hashmap={}
    for num in array:
        complement=target-num
        if complement in hashmap:
            return [complement,num]
        else:
            hashmap[num]=True
    return []