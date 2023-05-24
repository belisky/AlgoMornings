# Line Through Points...

- ## **_Category-Arrays_**
- ### **_Difficulty-veryHard_**

You're given an array of points on a 2D graph. Write a function that returns the maximum number of points that a single line passes through.

## Sample Input

---

points=[
[1,1],
[2,2],
[3,3],
[0,4],
[-2,6],
[4,0],
[2,1]
]

## Sample Output

---

4

## Approach to Solution

---

- I loop through an array of points.
- At each point, I loop through the whole array of points again and keep a hashmap of all possible slopes and how many times they occur.
- At the end, I return the maximum hashmap value in the hashmap.

### Time Complexity

---

- The time complexity of this approach is O(n^2).- where n is the number of points.

### Space Complexity

---

- The space complexity of this approach is O(n)
  where n is the number of points.

---

### One step at a time.
