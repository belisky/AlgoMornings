# Three Number Sort...

- ## **_Category-Sorting_**
- ### **_Difficulty-medium_**

You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain integers that are in the second array, and the second array rrepresents a desired order for the integers in the first array. For example, a second array of [x,y,z] represents a desired order of [x,x,...,x,y,y,...,y,z,z,...,z] in the first array.

Write a function that sorts the first array according to the desired order in the second array.

The function should perform this in place and it shouldn't use any auxiliary space


## Sample Input

---

```
array=[1,0,0,-1,-1,0,1,1]
order=[0,1,-1]
```

## Sample Output

---

```
[0,0,0,1,1,1,-1,-1]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n) time.

### Space Complexity

---

- The space complexity of this approach is O(1) space.

---

### One step at a time.
