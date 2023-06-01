# Minimum Height BST...

- ## **_Category-BST_**
- ### **_Difficulty-Medium_**

Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers and returns the root of the BST.

The function should minimize the height of the BST.

### Approach to Solution.

- Because the array is sorted in ascending order, it makes sense that the root of the BST is the element in the middle of the array.
- From there, all elements to the left of the middle element can form the left subTree because they are lesser than the middle element and all elements to the right of the middle element can form the right subTree because they are greater than teh middle element.
- So with the above premise in mind, we just call the Tree constructor in a manner such that at every point, it uses the middle element of the array as the root value and all elements to the left of the middle element as the leftSubTree and also all elements to the right of the middle element as the rightSubTree.

### Time Complexity

---

- The time complexity of this approach is O(n) where n is the length of the array.

### Space Complexity

---

- The space complexity of this approach is O(n)- where n is the length of the array.

### One step at a time.
