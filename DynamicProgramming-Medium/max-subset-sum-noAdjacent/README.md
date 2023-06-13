# Max Non Adjacent Sums...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Medium_**

Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.

## Sample Input

---

array=[75,105,120,75,90,135]

## Sample Output

---

30

## Approach to Solution

---

- I loop through the whole array; At each index, I try to calculate the maximum sum of elements before the current element which includes or doesn't include the current element.
- That means at each index, I know the maximum sum of non-adjacent elements including or not including the element at the current index.
- The way I can tell the maximum sum of non-adjacent elements at each index is by this formula;

  **maxSums[i]=max(maxSums[i-1],maxSums[i-2]+array[i]).**

- At the end of the whole iteration at the last index, I already have the maximum non adjacent sum.

### Time Complexity

---

- The time complexity of this approach is O(n).

### Space Complexity

---

- The space complexity of this approach is O(1)
  where n is the length of the hashmap and the quadruplets array.

### One step at a time.
