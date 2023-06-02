# Class Photos..

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

It's photo day at school and you are responsible for arranging the students in two rows before taking the photo. Each row should contain the same number of students and should adhere to the following guidelines: - All students wearing the same color should be in the same row. ie:: either blue or red should be grouped in two different rows respectively. - Each student in the back must strictly be taller than the student directly in front of them in the front row.

Write a function that returns whether or not a class photo that follows the guidelines above can be taken given two arrays each of heights of students in red shirts and heights of students in blue shirts.

## Sample Input

---

redShirtHeights=[5,8,1,3,4]
blueShirtHeights=[6,9,2,4,5]

## Sample Output

---

true

## Approach to Solution

---

- I sort both input arrays in ascending order and compare their last elements to see which group has the tallest last member.

- Based on the tallest last member, I loop through both arrays at once in a bid to find if the taller member at each iteration, is in the same group as the last tallest member.

### Time Complexity

---

- The time complexity of this approach is O(nlog(n))-- where n is equivalent to the number of students

### Space Complexity

---

- The space complexity of this approach is O(1).-

---

### One step at a time.
