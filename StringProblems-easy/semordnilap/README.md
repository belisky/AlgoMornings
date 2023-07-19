# Semordnilap...

- ## **_Category-Strings_**
- ### **_Difficulty-Easy_**

Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different string where the reverse of one word is the same as the forward version of the other. For example the words `diaper` and `repaid` are a semordnilap pair.

## Sample Input

---

```
words=['diaper','abc','test','cba','repaid']

```

## Sample Output

---

```
[[diaper,repaid],[abc,cba]]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\*m)- where n is the number of words and m is the length of the longest word.

### Space Complexity

---

- The space complexity of this approach is O(n\*m)- where n is the number of words and m is the length of the longest word.

---

### One step at a time.
