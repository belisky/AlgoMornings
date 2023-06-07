# Right Smaller Than...
![right-smaller-than](https://github.com/belisky/AlgoMornings/assets/61013338/66095bb5-b4a8-450b-a8fd-f397a48a5c14)

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

- I create a BST tree with an additional attribute of index.
- I create another class called TreeInfo with index and numberOfNodes less than as attributes.
- I then loop through the input array and at each iteration, I search the BST to see values that are
  smaller than the present value and whose index are larger than the index of the current value at that index.
- I store the count of all nodes that meet the above condition in numOfNodes and append that into an array.
- I output the array as my answer.

### Time Complexity

---

- The time complexity of this approach is O(nlog(n)).

### Space Complexity

---

- The space complexity of this approach is O(n)
  where n is the length of the array.

### One step at a time.
