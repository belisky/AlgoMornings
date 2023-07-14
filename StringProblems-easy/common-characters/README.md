# Common Characters...

- ## **_Category-Strings_**
- ### **_Difficulty-Easy_**

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity.
NB: strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.

## Sample Input

---

```
strings=[abc,bcd,cbaccd]

```

## Sample Output

---

```
[b,c]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(nm)- where n is the number of strings and m is the length of the longest string.

### Space Complexity

---

- The space complexity of this approach is O(m)

---

### One step at a time.
