# Nth Fibonacci...

- ## **_Category-Recursion_**
- ### **_Difficulty-easy_**

Write a function that takes in a special array and returns its product sum.

A special array is a non-empty array that contains either integers or other special arrays. The product sum of a special array is teh sum of its elements, where special arrays inside it are summed themselves and then multiplied by their level of depth

Eg; [[[]]] the depth of the innermost is 3 and the middle is 2 and the outter is 1.

## Sample Input

---

```
array=[5,2,[7,-1],3,[6,[-13,8],4]]
```

## Sample Output

---

```
12
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n) time-where n is the total number of elements in the array including sub-elements.

### Space Complexity

---

- The space complexity of this approach is O(d) space- where d is the greatest depth of the special arrays in the array.

---

### One step at a time.
