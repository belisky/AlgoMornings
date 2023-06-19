# Number of Ways to Traverse Graph...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Medium_**

You're given two positive integers representing the width and height of a grid-shaped, rectangular graph. Write a function that returns the number of ways to reach the bottom right corner of the grpah when starting at the top left corner. Each move you take must either go down or right. In other words, you can never move up or left in the graph.

## Sample Input

---

width=2
height=3

## Sample Output

---

3 // 1. Down,Down, Right && 2.Right,Down,Down && 3. Down,Right,Down.

## Approach to Solution

---

- I create an array of dimension+1 as the input array with 0's as elements to cater for 0 indexing.
- I then initialize every point at the edges of the array to become 1.
- The number of ways to reach a particular cell is just the sum of the cell above it and the cell to the left of it.

```
    waysLeft=numOfWays[heightIdx][widthIdx-1]
    waysUp=numOfWays[heightIdx-1][widthIdx]
    numOfWays[heightIdx][widthIdx]=waysLeft+waysUp

```

- I return the last item in the ways array as an answer.

### Time Complexity

---

- The time complexity of this approach is O(w\*h)- where w is the width and h is the height of the input array respectively.

### Space Complexity

---

- The time complexity of this approach is O(w\*h)- where w is the width and h is the height of the input array respectively.

### One step at a time.
