# Longest SubArray with Sum...

- ## **_Category-Arrays_**
- ### **_Difficulty-Hard_**

Write a function that finds the longest subarray where the values collectively sum up to the targetSum. Return an array of the starting Index and ending Index of this subArray, both inclusive.

## Sample Input

---

array=[1,2,3,4,3,3,1,2,1,2]
targetSum=10

## Sample Output

---

[4,8]

## Approach to Solution

---

- Using the sliding window technique, I keep 2 pointers which represents the start and ending index of the subarray.
- I expand the endingIndex until the the sum of elements between the starting and ending index is more than the target sum then,
- I close the startingIndex until the the sum of elements between the indices is less than or equal to the targetSum and I take note of the indices.
- I return the widest range that equals the targetSum.

### Time Complexity

---

- The time complexity of this approach is O(n).

### Space Complexity

---

- The space complexity of this approach is O(1)

### One step at a time.
