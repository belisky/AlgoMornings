# Generate Div Tags...

- ## **_Category-Recursion_**
- ### **_Difficulty-Hard_**

Write a function that takes in a positive integer `numberOfTags` and returns a list of all the valid string that you can generate with that number of matched `<div></div>` tags.

A string is valid and contains matched `<div></div>` tags if for every opening tag, there's a closing tag that comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should contain exactly `numberOfTags` opening tags and `numberOfTags` closing tags.
 
## Sample Input

---

```
numberOfTags=3
```

## Sample Output

---

```
[
    '<div><div><div></div></div></div>',
    '<div><div></div><div></div></div>',
    '<div><div></div></div><div></div>',
    '<div></div><div><div></div></div>',
    '<div></div><div></div><div></div>',

]

```

## Approach to Solution

---

### Time Complexity

---

- O((2n)!/((n!((n+1)!)))) time

### Space Complexity

---

- O((2n)!/((n!((n+1)!)))) space

---

### One step at a time.
