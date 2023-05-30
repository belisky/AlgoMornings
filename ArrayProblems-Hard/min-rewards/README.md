# Minimum Rewards...

- ## **_Category-Arrays_**
- ### **_Difficulty-Hard_**

Imagine that you're a teacher who's just graded the final exam in a class. You decide to reward your students fairly by giving them arbitrary rewards following two rules.

1. Students must receive at least one reward.
2. Any student must receive strictly more rewards than an adjacent student with a lower score and must receive fewer rewards than an adjacent student with a higher score.

Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules.

## Sample Input

---

scores=[,4,2,1,3,6,7,9,5]

## Sample Output

---

25

## Approach to Solution

---

- I loop through the scores twice; First from left to right and then from right to left.
- From Left to right:
  - I check if the score preceding is less than and set the current reward to the preceeding reward+1
- From Right to Left:
  - I check if the score after the current score is greater and I set the reward as the maximum of the current reward or the reward from the previous loop.

### Time Complexity

---

- The time complexity of this approach is O(n).

### Space Complexity

---

- The space complexity of this approach is O(n)
  where n is the length of the scores rewards array

### One step at a time.
