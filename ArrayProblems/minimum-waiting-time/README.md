# Minimum Waiting Time...

- ## **_Category-Greedy-Algorithms_**
- ### **_Difficulty-Easy_**

You're given a non-empty array of positive integers representing the amounts of time that specific queries take to execute. Only one query can be executed at a time, but they can be executed in any order.

A query's waiting time is defined as the amount of time it must wait before its execution starts.

Write a function that returns the minimum amount of total waiting time for all of the queries.

NB: you're allowed to mutate the input array.

## Sample Input

---

array=[3,2,1,2,6]

## Sample Output

17

## Approach to Solution

---

- I sort the queries and loop through them until the last but one query
- At every index, I add the time it takes to execute queries cummulatively and append that sum to a sums array.
- I then return the sum of the sums array.

### Time Complexity

---

- The time complexity of this approach is O(nlogn).
  where n is the number of queries

### Space Complexity

---

- The space complexity of this approach is O(1).

---

### One step at a time.
