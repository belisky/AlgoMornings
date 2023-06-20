# Maximum Sum Increasing subSequence...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

Write a function that takes in a no-empty array of integers and returns the great sum that can be generated form a strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.

## Sample Input

---

array=[10,70,20,30,50,11,30]

## Sample Output

---

[110, [10,20,30,50]] // The subsequence [10,20,30,50] is strictly increasing and yields the greatest sum from the array.

## Approach to Solution

---

- I create an IncreasingSumsAtIndex array which stores the biggest increasing sum of the subArray at or before that index.
- Accompanied with this array is another array called sequences, that references the index of the last element that was added to the increasing subArray to make it maximum.
- At the end of the iteration, I backtrack through the sequences array to find the elements that were responsible for the maxsumIncreasingSubsequence using the buildSeq function.

### Time Complexity

---

- The time complexity of this approach is O(n^2)

### Space Complexity

---

- The space complexity of this approach is O(n).

### One step at a time.
