# Same BSTs...
![same-bsts](https://github.com/belisky/AlgoMornings/assets/61013338/4ab83c46-0328-4de8-bfe1-81c7be81f27d)


- ## **_Category-BST_**
- ### **_Difficulty-Hard_**

An array of integers is said to represent the BST obtained by inserting each integer in teh array, from left to right into the BST.

Write a function that takes in two arrays of integers and determine whether these arrays represent the same BST. Note that you're not allowed to construct any BSTs in your code.

## Sample Input

---

arrayOne=[10,15,8,12,94,81,5,2,11]
arrayTwo=[10,8,5,15,2,12,11,94,81]

## Sample Output

---

true

## Approach to Solution

---

- I try to find the leftSubTree and the rightSubTree with the first element in the array as the root value.
- I then compare the leftSubTree's of both arrays and also the rightSubTree's of both arrays using a recursive approach that finds the leftSubTree and rightSubTree of the subsequent children of the root node.

### Time Complexity

---

-The time complexity of this approach is O(n\*\*2). where n is the number of nodes.

### Space Complexity

---

-The space complexity of this approach is O(d) where d is the depth of the BST that they represent.

### One step at a time.
