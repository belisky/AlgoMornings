# First Duplicate Value..

- ## **_Category-Arrays_**
- ### **_Difficulty-Medium_**

Given an array of integers between 1 and n inclusive where n is the length of the array.

- Write a function that returns the first integer that appears more than once.
  NB: You are not allowed to mutate the input array.

## Sample Input

---

array=[1,2,4,5,1,5]

## Sample Output

---

1

## Approach to Solution

---

- I loop through the array using each element as an index since every member of the array is within the range of n,
- At each iteration, I find the array element at that index and check if its negative.
- If the array element is negative that means I've already seen it earlier in the array hence I return it.
- If not, I negate the array element at that index.
- NB: array[index-1] translation because arrays are '0' indexed in python.

### Time Complexity

---

The time complexity of this approach is O(n)

### Space Complexity

---

- The space complexity of this approach is O(1).-

---

### One step at a time.
