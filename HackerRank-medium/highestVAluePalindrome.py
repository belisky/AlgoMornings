# O(n) space and time complexity
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    l,r=0,n-1
    marker=[0]*n
    s=list(s)
    while l<=r:
        if s[l]!=s[r]:
            if s[l]>s[r]:
                s[r]=s[l]
                marker[r]=1
            else:
                s[l]=s[r]
                marker[l]=1
            k-=1
        l+=1
        r-=1
    if k<0:
        return '-1'
    l,r=0,n-1
    while l<=r:
        if l==r and k>=1:
            s[l]='9'
            break
        if s[l]<'9':
            if marker[l]==0 and marker[r]==0 and k>=2:
                s[l]=s[r]='9'
                k-=2
            if (marker[l]==1 or marker[r]==1) and k>=1:
                s[l]=s[r]='9'
                k-=1
        l+=1
        r-=1
    return ''.join(s)