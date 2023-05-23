# Minimum Area Rectangle...

- ## **_Category-Arrays_**
- ### **_Difficulty-veryHard_**

You are given an array of points plotted on a 2D graph.
Write a function that returns the minimum area of any rectangle that can be formed using any 4 of these points such that the rectangle's sides are parallel to the x and y axes. If no rectangle can be formed, your function should return 0.

## Sample Input

---

points=[
[1,5],
[5,1],
[4,2],
[2,4],
[2,2],
[1,2],
[4,5],
[2,5],
[-1,-2],
]

## Sample Output

---

3 // the rectangle with corners [1,5], [2,5],[1,2],[2,2]

## Approach to Solution

---

- I initially create a set of all points in the input array.
- I iterate through the points input.
- At each point, I loop through previous points to see if they are diagonal to the current point and checking if that diagonal pair is within the PointsSet I created earlier.
- If there exists a diagonal pair I calculate the area and return the minimum area amongst the successful diagonal pairs.

### Time Complexity

---

-The time complexity of this approach is O(n^2).- where n is the length of the input array.

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the input array.

---

### One step at a time.
