# Maximum Sum Submatrix...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

You're given a two-dimensional array matrix of potentially unequal height and width that's filled with integers. You're also given a positive integer size. Write a function that returns the maximum sum that can be generated from a submatrix with dimensions `size*size`

## Sample Input

---

```
matrix =
[
    [5,3,-1,5],
    [-7,3,7,4],
    [12,8,0,0],
    [1,-8,-8,2]
]

size=2
```

## Sample Output

---

```
18
[
    [.,.,.,.],
    [.,3,7,.],
    [.,8,0,.],
    [.,.,.,.]
]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(w\*h) where w is the width of the matrix and h is the height of the matrix

### Space Complexity

---

- The space complexity of this approach is O(w\*h) where w is the width of the matrix and h is the height of the matrix

### One step at a time.
