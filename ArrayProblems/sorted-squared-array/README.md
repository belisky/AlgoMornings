# Two-Number-Sum...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

Write a function that takes an array with elements in ascending order and returns the squares of the elements as an array also in ascending order.

## Sample Input

---

array=[-3,1,2,5]

## Sample Output

---

[1,4,9,25]

## Approach to Solution

---

- I initialize an array the same size as the input array and keep a pointer on it starting from the lastItem(pos).
- I use the two pointer approach where one pointer points to the beginning of the input array(min) and another pointer points to the end of the input array(max)
- Using a while loop, i iterate throught the input array, comparing the absolute values of the elements located at min and max pointers respectively.
- The greater element gets squared and is inserted at the index of pos.
- If it is the element pointed to by min that got squared, min pointer increases
- If it is the element pointed to by max that got squared, max pointer decreases.
- Pos then decreases regardless of which element got squared.

### Time Complexity

---

-The time complexity of this approach is O(n).

### Space Complexity

---

-The space complexity of this approach is O(1)

---

### One step at a time.
