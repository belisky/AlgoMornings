# Maximum profit with K Transactions...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-veryHard_**

You're given an array of positive integers representing the prices of a single stock on various days (each index in the array represents a different day). You're also given an integer `k`, which represents teh number of transactions you're allowed to make. One transaction consists of buying the stock on a given day and selling it on another day.

Write a function that returns the maximum profit that you can make by buying and selling the stock, given k transactions.

## Sample Input

---

```
prices=[5,11,3,50,60,90]
k=2

```

## Sample Output

---

```
93 // Buy:5, Sell:11; Buy:3, Sell:90
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\*k)- where n is the number of prices and k is the number of transactions.

### Space Complexity

---

- The space complexity of this approach is O(n\*k)- where n is the number of prices and k is the number of transactions.

### One step at a time.
