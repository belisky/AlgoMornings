# Juice Bottling...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

You're given an array of integer prices of length n with the retail prices of various quantities of juice. Each index in this array corresponds to the price of that amount of juice. For example, prices[2] would be the retail price of 2 units of juice.

You have `n-1` total units of juice. For example, if the length of `prices` is 5, then you would have 4 total units of jice. Write a function to determine the optimal way to bottle the huice such that it maximizes revenue. This function should return a list of all the huice quantities required in ascending order.

## Sample Input

---

```
prices=[0,1,3,2]
```

## Sample Output

---

```
[1,2]

```

## Approach to Solution

---

- I first loop through the length of the array.
- At each point, I try to see if there are dividingPoints at that index that maximizes the profit of that particular index.

```
 for size in range(numSizes):
        for dividingPoint in range(size+1):
            possibleProfit=maxProfit[size-dividingPoint]+prices[dividingPoint]

            if possibleProfit>maxProfit[size]:
                maxProfit[size]=possibleProfit
                solutions[size]=[dividingPoint]+solutions[size-dividingPoint]

```

- I then return the last element of the solutions array as an answer.

### Time Complexity

---

- The time complexity of this approach is O(n^2) where n is the length of prices.

### Space Complexity

---

- The space complexity of this approach is O(n)

### One step at a time.
