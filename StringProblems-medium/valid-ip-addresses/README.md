# Valid IP Addresses...

- ## **_Category-Strings_**
- ### **_Difficulty-Medium_**

You're given a string of length of 12 or smaller, containing only digits. Write a function that returns all the possible IP addresses that can be created by inserting three `.`s in the string.

An IP address is a sequence of four positive integers that are separated by `.`s, where each individual integer is within the range `0-255`, inclusive.

## Sample Input

---

```
string='1921680'

```

## Sample Output

---

```
[
    '1.9.216.80',
    1.92.16.80,
    1.92.168.0,
    19.2.16.80,
    19.2.168.0,
    19.21.6.80,
    19.21.68.0,
    19.216.8.0,
    192.1.6.80,
    192.1.68.0,
    192.16.8.0

]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(1) time.

### Space Complexity

---

- The space complexity of this approach is O(1) space.

---

### One step at a time.
