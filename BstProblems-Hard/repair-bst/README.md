# Repair BST...

- ## **_Category-BST_**
- ### **_Difficulty-Hard_**

Write a function that takes in a BST where two values have been swapped and returns the repaird tree with all values on teh correct nodes.

## Sample Input

---

## Sample Output

## Approach to Solution

---

- I traverse throught the tree recursively using inOrder traversal.
- I keep pointers of 2 nodes that are misplaced and a third node that keeps track of the previousVisitedNode in the BST.
- To find the first misplaced node, check if the previousNode is bigger than the currentNode. that is your first misplaced Node.
- To find your second misplaced node, check if there's a first misplaced node, if there exists a first misplaced node, that means you have found your second misplaced node, using the same condition that a node is misplaced if the previousNodeValue is bigger than the currentNodeValue.
- You then swap the misplacedNode values to solve the problem.

### Time Complexity

---

-The time complexity of this approach is O(n). where n is the number of nodes.

### Space Complexity

---

-The space complexity of this approach is O(h) where h is the height of the BST.

### One step at a time.
