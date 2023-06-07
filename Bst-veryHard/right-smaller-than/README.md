# Right Smaller Than...

- ## **_Category-BST_**
- ### **_Difficulty-veryHard_**

Write a function that takes in an array of integers and returns an array of the same length, where each element in the output array correponds to the number of integers in the input array that are to the right of the relevant index and that are strictly smaller than the integer at that index.

## Sample Input

---

array=[8,5,11,-1,3,4,2]

## Sample Output

---

[5,4,4,0,1,1,0]

## Approach to Solution

---

- I loop through the whole array using pointer i.
- At every particular element that i points to, I loop through from the position of index i using index j.
- I count the number of elements referenced by j that are less than the element referenced by i.
- I store the counts in an array after every inner loop and return it as the answer.

### Time Complexity

---

-The time complexity of this approach is O(n\*\*2).

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the array.

### One step at a time.
