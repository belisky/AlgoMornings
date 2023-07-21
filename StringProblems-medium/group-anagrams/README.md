# Group Anagrams...

- ## **_Category-Strings_**
- ### **_Difficulty-Medium_**

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. for example, `cinema` and `iceman` are anagrams.

## Sample Input

---

```
words=['yo','act','flop','tac', 'foo','cat','oy','olfp']

```

## Sample Output

---

```
[['yo','oy'],['flop','olfp'],['act','tac','cat'],['foo']]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(w*n*log(n)) - where w is the number of words and n is the length of the longest word.

### Space Complexity

---

- The space complexity of this approach is O(wn) - where w is the number of words and n is the length of the longest word.

---

### One step at a time.
