# Number of Ways to Make Change...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Medium_**

Given an array of distinct positive integers representing coin denominations and a single positive interger n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denomination.

## Sample Input

---

n=6
denoms=[1,5]

## Sample Output

---

2 // 1x1 + 1x5 AND 6x1

## Approach to Solution

---

### Caveat: There are 1 ways to make a change of 0 amount.

- I loop through all the coin denominations given to me.
- At each coin denomination, I loop through the range of the input amount.
- At each iteration of the input amount, I check if the particular coin can be used to make a change at that amount;

**if target_amount>=coin_denomination**

- - NB: A coin can be used in a change for an amount if the amount is bigger than the coin.
- If the coin can be used, I compute the number of ways by which you can make a change using this formula:

**ways[target_amount]+=ways[target_amount-coin_denomination]**

- I return the last item in the ways array as an answer.

### Time Complexity

---

- The time complexity of this approach is O(nd)- where n is the target amount and d is the number of coin denominations.

### Space Complexity

---

- The space complexity of this approach is O(n)

### One step at a time.
