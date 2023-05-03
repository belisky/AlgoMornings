# Two-Number-Sum...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

This is a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function finds a pair in the array that sum up to the target sum and returns an array of the pair.

## Sample Input

---

array=[7,6,4,-1]
targetSum=10

## Sample Output

---

[6,4]

## Approach to Solution

---

- I loop through the whole array.
- At every particular element that i points to, I find the difference and check if its in a hashmap.
- If its there I return the difference and the array element
- if not, I add that array element to the hashmap

### Time Complexity

---

-The time complexity of this approach is O(n).

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the hashmap and the quadruplets array.

---

### One step at a time.
