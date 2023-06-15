# Minimum Number of Coins to make a change...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Medium_**

Given an array of positive integers representing coin denominations and a single positive integer representing a target amount. Write a function that returns the smallest number of coins needed to make change for that target amount using the given coins.

Return -1 if it's impossible to make change for the amount.

## Sample Input

---

n=7
denoms=[1,5,10]

## Sample Output

---

3 // 2x1 + 1x5

## Approach to Solution

---

- I initialize an array the same length as the target amount+1 with values as _inf_.
- The first array element is set to 0 because, the number of coins needed to make a change of 0 is 0
- I loop through all the coin denominations given to me.
- At each coin denomination, I loop through the range of the coin to the input amount.
- Since my inner for loop starts at the denomination and ends at the target amount, it means that denomination can be used to make change for the range of those amounts.
- I just choose the minimum coins needed to make change at that amount using the formula:
  **numOfCoins[amount]=min(numOfCoins[amount],numOfCoins[amount-denom]+1)**

- I return the last item in the array as an answer if it exits or -1.

### Time Complexity

---

- The time complexity of this approach is O(nd)- where n is the target amount and d is the number of coin denominations.

### Space Complexity

---

- The space complexity of this approach is O(n)

### One step at a time.
