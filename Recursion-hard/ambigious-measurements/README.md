# Ambigious Measurements...

- ## **_Category-Recursion_**
- ### **_Difficulty-Hard_**

This problem deals with measuring cups that are missing important measuring labels. Specifically, a measuring cup only has two measuring lines, a Low(L) line and a High(H) line. This means that these cups can't precisely measure and can only gurantee that the substance poured into them will be between the L and H line. For example, you might have a measuring cup that has a Low line at `400ml` and a high line at `435ml`. This means that when you use this measuring cup, you can only be sure that what you're measuring is between 400ml and 435ml.

You're given a list of measuring cups containing their low and high lines as well as one low integer and one high integer representing a range for a target measurement. Write a function that returns a boolean representing whether you can use the cups to accurately measure a volume in the specified [low,high] range(the range is inclusive).


## Sample Input

---

```
measuringCups=[
    [200,210],
    [450,465],
    [800,850]
]
low=2100
high=2300

```

## Sample Output

---

```
true

```

## Approach to Solution

---

### Time Complexity

---

- O(low*high*n) time- where n is the number of measuring cups.

### Space Complexity

---

- O(low*high) space

---

### One step at a time.
