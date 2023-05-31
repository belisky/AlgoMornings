# Validate BST...

- ## **_Category-BST_**
- ### **_Difficulty-Medium_**

Write a function that takes in a potentially invalid Binary Search Tree and returns a boolean representing whether the BST is valid.

A node is said to be valid BST if its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or Null.

A BST is valid if and only if all of its nodes are valid BST nodes.

### Approach to Solution.

I use depth first search to iterate through all nodes in the tree.

- At each node, I check if that node is a validate bst by checking its left sub tree and its right sub tree using recursion.
- At the left sub tree, the node should have the biggest value and the smallest value there can ever be in the left sub tree is **float(-inf)**. So I check if the node's value fits a valid BST. **_node>leftSubTree_** [dfs(lower,tree.value,tree.left)]
- At the rightSubTree, the node should have the smallest value and the largest value there can ever be in the rightSubTree is **float(inf)** So I check if the nodes value fits a valid BST for the rightSubTree too. **_node<=rightSubTree_** [dfs(tree.value,upper,tree.right)]

### Time Complexity

---

- The time complexity of this approach is O(n) where n is the number of nodes in the BST.

### Space Complexity

---

- The space complexity of this approach is O(d)- where d is the depth(height) of the BST.

### One step at a time.
