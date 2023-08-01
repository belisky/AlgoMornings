# Pattern Matcher...

- ## **_Category-Strings_**
- ### **_Difficulty-Hard_**

You're given two non-empty strings. The first one is a pattern consisting of only 'x' and or 'y'; the other one is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern.

## Sample Input

---

```
pattern='xxyxxy'
string='gogopowerrangergogopowerranger'
```

## Sample Output

---

```
['go','powerranger']
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n^2+m)- where n is the length of the main string and m is the length of the pattern

### Space Complexity

---

- The space complexity of this approach is O(n+m) space.

---

### One step at a time.
