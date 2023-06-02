# Two-Number-Sum...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence is a set of numbers that are not necessarily adjacent in the array but are in the same order as they appear in the array.

## Sample Input

---

array=[5,1,22,25,6,-1,8,10]
sequence=[1,6,-1,10]

## Sample Output

---

true

## Approach to Solution

---

- I loop through both arrays simultaneiously using two different indexes, one for the array(arrIdx) and one for sequence(seqIdx).
- If both elements in the arrays match, seqIdx is increased as well as arrIdx.
- If there's no match between array elements, only arrIdx is increased.
- To verify that sequence is really a subsequence of array, I check if seqIdx equals the lenght of the sequence. that shows that we found all the sequence elements in the array.

### Time Complexity

---

-The time complexity of this approach is O(n).

### Space Complexity

---

-The space complexity of this approach is O(1)

---

### One step at a time.
