# PowerSet...

- ## **_Category-Recursion_**
- ### **_Difficulty-medium_**

Write a function that takes in an array of unique integers and returns its powerset.

The powerset `P(X)` of a set `X` is the set of all the subsets of `x`. For example, the powerset of `[1,2]` is `[[],[1],[2],[1,2]]`

Note that the sets in the powerset do not need to be in any particular order.

## Sample Input

---

```
array=[1,2,3]
```

## Sample Output

---

```
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\*2^n) time.-where n is the length of the input array.

### Space Complexity

---

- The space complexity of this approach is O(n\*2^n) space.

---

### One step at a time.
