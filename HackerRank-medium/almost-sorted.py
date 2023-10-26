from copy import *

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#O(nlogn)

def almostSorted(arr):
    tmp=deepcopy(arr)
    tmp.sort()
    if arr==tmp:
        print('yes')
        return
    n=len(arr)
    l=r=-1
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            l=i
            break
    for j in range(n-1,0,-1):
        if arr[j]<arr[j-1]:
            r=j
            break
     
    tmp1=deepcopy(arr)
    tmp1[l],tmp1[r]=tmp1[r],tmp1[l]
    if tmp1==tmp:
        print('yes')
        print('swap',l+1,r+1)
        return
    tmp1=deepcopy(arr)
    tmp1=tmp1[:l]+tmp1[l:r+1][::-1]+tmp1[r+1:]
    if tmp1==tmp:
        print('yes')
        print('reverse',l+1,r+1)
        return
    print('no')
    # Write your code here


# #solution 2
# def almostSorted(arr):
#     arr_sorted = sorted(arr)
#     if arr_sorted == arr:
#         print('yes')
#     elif len(arr) <= 2:
#         print('yes')
#         print('swap 1 2')
#         return
        
#     diff = []
#     for i in range(len(arr)):
#         if arr[i] != arr_sorted[i]:
#             diff.append([arr[i], i])
    
#     if len(diff) == 2:
#         print('yes')
#         print('swap {} {}'.format(diff[0][1] + 1, diff[1][1] + 1))
        
#     elif len(diff) < 2:
#         print('no')
        
#     else:
#         seq = []
#         for i in diff:
#             seq.append(i[0])
#         rev = seq[::-1]
#         if sorted(rev) == rev:
#             print('yes')
#             print('reverse {} {}'.format(diff[0][1] + 1, diff[-1][1] + 1))
#         else:
#             print('no')