# Smallest Substring Containing...

- ## **_Category-Strings_**
- ### **_Difficulty-veryHard_**

You're given two non-empty strings: a big string and a small string. Write a function that returns the smallest substring in the big string that contains all of the small string's characters.

NB:

- The substring can contain other characters not found in the small string.
- The characters in the substring dont have to be in the same order as they appear in the small string.
- If the small string has duplicate characters, the substring has to contain those duplicate character(it can also contain more, but not fewer)

## Sample Input

---

```
bigString='abcd$ef$axb$c$'
smallString='$$abf'
```

## Sample Output

---

```
'f$axb$'
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(a+b)- where a is the length of the big string and b is the length of the small string.

### Space Complexity

---

- The space complexity of this approach is O(a+b)- where a is the length of the big string and b is the length of the small string.

---

### One step at a time.
