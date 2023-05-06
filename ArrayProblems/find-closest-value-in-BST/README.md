# Find closest Value in BST..

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

Write a function that takes in a BST and a target value and returns the closest value to that target in the BST. You can assume that there is only one closest value.

## Sample Input

---

coins= 10
/ \
 5 15
/ \ / \
 2 5 13 22
/ \
 1 14

target=12

## Sample Output

---

13

## Approach to Solution

---

- I traverse throught the tree using a helper function in a while loop.
- At each traversal, i compare the absolute difference between the target and the closest element and the absolute difference between the target and the current node value.
- If the absolute difference between the target and the current node value is smaller, i update the closest to be the current node value.
- I then traverse in the direction of the target depending on the current nodes value using the property of BST.
- If the target equals the current node value, I break out of the loop.

### Time Complexity

---

-The time complexity of this approach is O(logn)-- because of the sort.

### Space Complexity

---

-The space complexity of this approach is O(1).

---

### One step at a time.
