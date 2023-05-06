# Non-Constructible change...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**

Given an array of positive integers representing the values of coins you have, write a function that returns the minimum amount of change you cannot give. If you're given no coins, the minimum amount of change you cannot give is 1.

## Sample Input

---

coins=[5,7,1,1,2,3,22]

## Sample Output

---

20

## Approach to Solution

---

- I start by sorting the coins and initializing the current change I can give as 0.
- I then loop through the sorted coins.
- At each coin, I check if the coin is lesser than or equal to my **_current change +1_**. \_That means I can give that change and so my coin has no effect.
- On the other hand, if my coin is greater than the _current change +1_, that means I cant give a change which is equal to _current change+1_. Hence I return _current change+1_ as my answer.

### Time Complexity

---

-The time complexity of this approach is O(nlogn)-- because of the sort.

### Space Complexity

---

-The space complexity of this approach is O(1).

---

### One step at a time.
