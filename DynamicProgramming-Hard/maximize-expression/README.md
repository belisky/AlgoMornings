# Maximize Expression...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

Write a function that takes in an array of integers and returns the largest possible value for the expression `array[a]-array[b]+array[c]-array[d]`, where a,b,c,d are indices of the array and a<b<c<d.

## Sample Input

---

array=[3,6,1,-3,2,7]

## Sample Output

---

4
// Choose a=1,b=3,c=4,d=5
// -> 6-(-3)+2-7=4

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n) where n is the length of the array.

### Space Complexity

---

- The space complexity of this approach is O(n)- where n is the length of the array.

### One step at a time.
