# Knight Connection...

- ## **_Category-Arrays_**
- ### **_Difficulty-Hard_**

You're given the position of two knight pieces on an infinite chess board. Write a function that returns the minimum number of turns required before one of the knights is able to capture the other knight, assuming the knights are working together to achieve this goal.

A knight can move to any of these 8 locations on its next move:
[
[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]
]

## Sample Input

---

knightA=[0,0]
knightB=[4,2]

## Sample Output

---

1

## Approach to Solution

---

- Since this is essentially a graph problem I traverse throught the graph using bfs(queue) from only one knight position.
- If I am able to find the other knight's position from this one, I divide the number of moves it took into 2. and return that as the total number of moves since the Knights are assumed to be working together.

### Time Complexity

---

- The time complexity of this approach is O(n\*m)-- where n is the horizontal distance between the knights and m is the vertical distance between the knights.

### Space Complexity

---

- The space complexity of this approach is O(n\*m)-- where n is the horizontal distance between the knights and m is the vertical distance between the knights.

### One step at a time.
