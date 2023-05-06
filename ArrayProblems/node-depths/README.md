# Branch sums..

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

Write a function that takes a Binary Tree and returns a list of its branch sums ordered from leftmost to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

## Sample Input

---

coins= 1
/ \
 2 3
/ \ / \
 4 5 6 7
/ \ /
8 9 10

## Sample Output

---

[15,16,18,10,11]

## Approach to Solution

---

- I traverse throught the tree recursively(inOrderly).
- At each recursive call, I concatenate the return values of the recursive calls on the left-subTree and right-subTree as an array.
- The return value of each recursive call is such that, if the call below the current stack falls on a leaf node, it returns a single array with that leaf node as element.
- else the array elements returned from the recursive call beneath are each incremented by the value of the current node.
- And because the traversal is inOrder, the return value is just as we want it.

### Time Complexity

---

-The time complexity of this approach is O(n)-- where n is equivalent to the number of nodes on the binary tree which equals the number of times the recursive function is invoked

### Space Complexity

---

-The space complexity of this approach is O(n).--where n is the number of nodes on the binary tree

---

### One step at a time.
