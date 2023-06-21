# Longest Common Subsequence...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

Write a function that takes in two strings and returns their longest common subsequence.

A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as they appear in the string. For instance, the characters ['a','c','d'] form a subsequence of the string 'abcd', and so do the characters ['b','d']. Note that a sindle character in a string and the string itself are both valid subsequences of the string.

## Sample Input

---

str1='ZXVVYZW'
str2='XKYKZPW'

## Sample Output

---

[X,Y,Z,W]

## Approach to Solution

---

- I create an array that tracks the common subsequence called lcs

```
 lcs=[[[] for x in range(len(str1)+1)] for y in range(len(str2)+1) ]

```

- I loop through the first string using index i.
- At each iteration, I loop through the whole of the second string.
- if the strings at the i and j indexes are the same;

```
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1]==str1[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+[str2[i-1]]
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1],key=len)
    return lcs[-1][-1]
```

- I return the last item in the lcs array as an answer.

### Time Complexity

---

- The time complexity of this approach is O(w\*h)- where w is the width and h is the height of the input array respectively.

### Space Complexity

---

- The space complexity of this approach is O(w\*h)- where w is the width and h is the height of the input array respectively.

### One step at a time.
