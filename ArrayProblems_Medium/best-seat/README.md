# Best Seat...

- ## **_Category-Arrays_**
- ### **_Difficulty-Medium_**

You walk into a theatre and the usher walks you to your row and you are allowed to sit anywhere. You would like to sit in the seat that gives you most space and you would also prefer this space to be evenly distributed on either side of you.

Given a row as an integer array, return the seat of the index of where you should sit. 1's represent occupied seats and 0's are empty seats.

## Sample Input

---

seats=[1,0,1,0,0,0,1]

## Sample Output

---

4

## Approach to Solution

---

- I loop through the whole array.
- At every particular element that i points to, I find the difference and check if its in a hashmap.
- If its there I return the difference and the array element
- if not, I add that array element to the hashmap

### Time Complexity

---

-The time complexity of this approach is O(n).

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the hashmap and the quadruplets array.

---

### One step at a time.
