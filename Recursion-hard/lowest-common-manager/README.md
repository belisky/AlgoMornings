# Lowest Common Manager...

- ## **_Category-Recursion_**
- ### **_Difficulty-Hard_**

You're given three inputs, all of which are instances of an `OrgChart` class that have a `directReports` property pointing to their direct reports. The first input is the top manager in an organizational chart(ie: the only instance that isn't anybody else's direct report), and the other two inputs are reports in the organizational chart. The two reports are guaranteed to be distinct.

Write a function that returns the lowest common manager to the two reports.

## Sample Input

---

```
topManager= Node A
reportOne= Node E
reportTwo=Node I

       A
      / \
     B   C
    / \ / \
   D  E F  G
  / \
 H   I

```

## Sample Output

---

```
Node B
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\*n!) time.-where n is the length of the input array.

### Space Complexity

---

- The space complexity of this approach is O(n\*n!) space.

---

### One step at a time.
