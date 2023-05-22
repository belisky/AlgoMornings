# WaterFall-Streams...

- ## **_Category-Arrays_**
- ### **_Difficulty-veryHard_**

You are given a two-dimensional array that represents the structure of an indoor waterfall.
Each row in the array contains 0's(freespace) and 1's(Block).
As water flows downwards,if it hits a block, it splits evenly to the left and right of that block. If a water stream is unable to flow to the left or to the right, that stream becomes trapped and can no longer continue to flow.

Write a function that returns the percentage of water inside each of the bottom buckets after the water has flowed through the entire structure.

## Sample Input

---

array=[
[0,0,0,0,0,0,0],
[1,0,0,0,0,0,0],
[0,0,1,1,1,0,0],
[0,0,0,0,0,0,0],
[1,1,1,0,0,1,0],
[0,0,0,0,0,0,1],
[0,0,0,0,0,0,0]
]

source =3

## Sample Output

---

[0,0,0,25,25,0,0]

## Approach to Solution

---

- At each point in time, I loop through two adjacent rows at the same time, rowAbove and currentRow.
- I step through each cell for the row above.
- At each cell, I check if there's water in the cellAbove and also if the currentCell has an empty space or a block.
- If the currentCell has an empty space and the cellAbove has water, the water is automatically transferred into the currentCell.
- If the currentCell is a block, the water in the cellAbove is split with half flowing to the right and the other half flowing to the left.
- I check the currentCells to the left and right of the Block to see if they are empty spaces to collect the split water.
- I then update the rowAbove to become the currentRow and the currentRow becomes the next Row and I start the cycle all over again.

NB: Any cell that has water has a value of -ve

### Time Complexity

---

-The time complexity of this approach is O(w^2\*h).- where w and h represent the width and height of the array respectively

### Space Complexity

---

-The space complexity of this approach is O(w)
where w is the width of the array.

---

### One step at a time.
