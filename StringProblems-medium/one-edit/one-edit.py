def oneEdit(stringOne, stringTwo):
    lengthOne,lengthTwo=len(stringOne),len(stringTwo)
    if abs(lengthOne-lengthTwo)>1:
        return False
    madeEdit=False
    indexOne=0
    indexTwo=0

    while indexOne<lengthOne and indexTwo<lengthTwo:
        if stringOne[indexOne]!=stringTwo[indexTwo]:
            if madeEdit:
                return False
            madeEdit=True
            if lengthOne>lengthTwo:
                indexOne+=1
            elif lengthTwo>lengthOne:
                indexTwo+=1
            else:
                indexOne+=1
                indexTwo+=1
        else:
            indexOne+=1
            indexTwo+=1
    # Write your code here.
    return True


# # 2nd Solution
# def oneEdit(stringOne, stringTwo):
#     len1,len2=len(stringOne),len(stringTwo)
#     # if abs(len1-len2)>1:
#     #     return False
        
#     for i in range(min(len1,len2)):
#         if stringOne[i]!=stringTwo[i]:
#             if len1>len2:
#                 return stringOne[i+1:]==stringTwo[i:]
#             elif len2>len1:
#                 return stringTwo[i+1:]==stringOne[i:]
#             else:
#                 return stringOne[i+1:]==stringTwo[i+1:]
   
#     return True
