# Three-Number-Sum...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

This is a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function finds a 3 numbers in the array that sum up to the target sum and returns an array of the pair.

## Sample Input

---

array=[12,3,1,2,-6,5,-8,6]
targetSum=0

## Sample Output

---

[[-8,3,5],[-8,2,6],[-6,1,5]]

## Approach to Solution

---

- I loop through the whole array with a pointer i.
- At every particular element that i points to, I use a two pointer approach on an already sorted array.
- One pointer(left) starts after i and the other(right) starts at the end of the array.
- if the sum of elements at i,left and right sum up to target, I add the triplets to an array if not, I move the left pointer if the sum is less than the target or I move the right pointer if the sum is more than the target.
- If the sum equals target I move i, increase left and decrease(closein) from the right.

### Time Complexity

---

-The time complexity of this approach is O(n\*\*2).

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the hashmap and the quadruplets array.

---

### One step at a time.
