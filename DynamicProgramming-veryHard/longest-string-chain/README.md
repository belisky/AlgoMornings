# Longest String Chain...

## Catergory: Dynamic Programming.

## Difficulty: **veryHard**

Given a list of strings, write a function that returns the longest tring chain that can be build from those strings.

## Sample Input

---

```
strings=['abde',abc,adb,abcde,ade,ae,1abde,abcdef]

```

## Sample Output

---

```
[abcdef,adbde,abde,ade,ae]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n \* m^2 + nlog(n))- where n is the number of strings and m is the length of the longest string.

### Space Complexity

---

- The space complexity of this approach is O(nm)

### One step at a time.
