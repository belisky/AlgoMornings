# Square of Zeroes...

## Category: Dynamic Programming..

## Difficulty: veryHard..

Write a function that takes in a square-shaped nxn two-dimensional array of only 1s and 0s and returnss a boolean representing whether the input matrix contains a square whose borders are made up of only 0s.

NB: a 1x1 square doesn't count as a valid square.

## Sample Input

---

```
matrix=[
    [1,1,1,0,1,0],
    [0,0,0,0,0,1],
    [0,1,1,1,0,1],
    [0,0,0,1,0,1],
    [0,1,1,1,0,1],
    [0,0,0,0,0,1],
]

```

## Sample Output

---

```
true
[
    [ , , , , , ],
    [0,0,0,0,0, ],
    [0, , , ,0, ],
    [0, , , ,0, ],
    [0, , , ,0, ],
    [0,0,0,0,0, ],
]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\^4)- where n is the length of the matrix.

### Space Complexity

---

- The space complexity of this approach is O(1)

### One step at a time.
