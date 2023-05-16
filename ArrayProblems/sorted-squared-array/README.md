# Sorted Squared Array...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**
![sortedSquares](https://github.com/belisky/AlgoMornings/assets/61013338/9e98177a-c139-4b60-9478-cadb23236191)


Write a function that takes an array with elements in ascending order and returns the squares of the elements as an array also in ascending order.

## Sample Input

---

array=[-3,1,2,5]

## Sample Output

---

[1,4,9,25]

## Approach to Solution

---

- I initialize an array the same size as the input array and keep a pointer on it starting from the lastValueIndex.
- I use the two pointer approach where one pointer points to the beginning of the input smallerValueIndex and another pointer points to the end of the input array largetValueIndex.
- Using a while loop, i iterate throught the input array, comparing the absolute values of the elements located at smallerValueIndex and the largeValueIndex respectively.
- The greater element gets squared and is inserted at the index of currentPointer.
- If it is the element pointed to by smallerValueIndex that got squared, smallerValueIndex increases
- If it is the element pointed to by largerValueIndex that got squared, largerValueIndex decreases.
- CurrentPointer then decreases regardless of which element got squared.

### Time Complexity

---

- The time complexity of this approach is O(n).

### Space Complexity

---

- The space complexity of this approach is O(n)

---

### One step at a time.
