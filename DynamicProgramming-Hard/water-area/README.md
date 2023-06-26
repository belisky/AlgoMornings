# Water Area...
![water-area](https://github.com/belisky/AlgoMornings/assets/61013338/8c7eabb9-7f6b-4456-a307-19ad47ca381f)

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

You're givven an array of non-negative integers where each non-zero integer represents the height of a pillar of width 1. Imagine water being poured over all of the pillars; write a function that returns the surfae area of water trapped between the pillars viewed from the front. Note that spilled water should be ignored.

## Sample Input

---

heights=[0,8,0,0,5,0,0,10,0,0,1,1,0,3]

## Sample Output

---

48

## Approach to Solution

---

- I create an array called maxes that tracks the highest pillar to the left and right of a particular index.

- I then loop through the array from left to right, at each index I compare the height with the leftMax(which is the maximum height found so far). I then keep the leftMax in the maxes array.

```
    maxes=[0 for _ in heights]
    leftMax=0
    for i in range(len(heights)):
        height=heights[i]
        maxes[i]=leftMax
        leftMax=max(leftMax,height)
```

- Again I loop from right to left and this time I am doing two things at once:
  - The first is finding the highest value(rightMax) to the right of the current index.
  - The second is after finding the hightest element, I compare the rightMax to the leftMax which is already in maxes.
  - I then compare if the height of the current index is lesser than the minimum of the rightMax and leftMax.
    - If its less it means that particular height can hold water of value min(rightMax,leftMax)-height and store that value as the new value in maxes.
    ```
       for i in reversed(range(len(heights))):
    height=heights[i]
    minHeight=min(rightMax,maxes[i])
    if height<minHeight:
        maxes[i]=minHeight-height
    else:
        maxes[i]=0
    rightMax=max(rightMax,height)
    ```
- I return the sum of maxes as the answer.

### Time Complexity

---

- The time complexity of this approach is O(n)

### Space Complexity

---

- The space complexity of this approach is O(n)

### One step at a time.
