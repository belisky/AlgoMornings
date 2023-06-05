# Same BSTs...

- ## **_Category-BST_**
- ### **_Difficulty-Hard_**

You're given three nodes that are in the same BST: nodeOne,nodeTwo, and nodeThree. Write a function that returns the boolean representing whether one of nodeONe or nodeThree is an ancestor of nodeTwo. Meaning check whether if nodeTwo is inbetween nodeOne and nodeThree in the BST.
ie: check if nodeOne->nodeTwo->nodeThree or
nodeThree->nodeTwo->nodeOne.

## Sample Input

---

tree= 5
/ \
 2 7
/ \ / \
 1 4 6 8
/ /
0 3

nodeOne=5
nodeTwo=2
nodeThree=3

## Sample Output

---

true

## Approach to Solution

---

- I try to find if nodeTwo is a child of nodeOne, if it is, I continue to find if nodeThree is a child of nodeTwo and vice versa starting with if nodeTwo is a child of nodeThree...

### Time Complexity

---

-The time complexity of this approach is O(d). where d is the distance between nodeOne and nodeThree.

### Space Complexity

---

- The space complexity of this approach is O(1)

### One step at a time.
