# Disk Stacking...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

You're given a non-empty array of array where each subarray holds three integers and represents a disk. These integers denote each disk's width,depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the stack. A disk must have a strictly smaller width,depth, and height than any other disk below it.

Write a function that return an array of the disks in the final stack, starting with the top dissk and endind with the bottom disk. Note that you can't rotate disks; In other words, the integers in each subarray mut represent [width,depth,height] at all times.

## Sample Input

---

disks=[[2,1,2],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5]]

## Sample Output

---

[[2,1,2],[3,2,3],[4,4,5]]

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\^2)- where n is the number of disks.

### Space Complexity

---

- The space complexity of this approach is O(n)- where n is the number of disks

### One step at a time.
