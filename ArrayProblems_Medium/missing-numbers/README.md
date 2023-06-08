# Missing Numbers..
![missing-numbers](https://github.com/belisky/AlgoMornings/assets/61013338/04e74519-f325-49c6-84d2-29765f36d3ad)

- ## **_Category-Arrays_**
- ### **_Difficulty-Medium_**

You're given an unordered list of unique integers 'nums' in the range of [1,n], where n is the length of nums+2. This means that two numbers are missing from the list.

Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically.

## Sample Input

---

nums=[1,4,3]

## Sample Output

---

[2,5]

## Approach to Solution

---

- Since I know the total range, I calculate the sum of the total range and subtract the sum of nums array from it.
- This leaves me with the sum of the missing numbers. I then find the average of the missing numbers.
- Since I know the average of the missing numbers, I loop through the nums list to find the sum of numbers that are greater than the average and less than the average respectively.
- I subtract the sum of numbers less than the average from the expectedAverage in range[1,avgValue+1] to get the first missing number.
- I subtract the sum of numbers greater than the average from the expectedAverage in range[avgValue+1,len(nums)+3] to get the second missing number.

### Time Complexity

---

- The time complexity of this approach is O(n)-- where n is equivalent to the length of the input array

### Space Complexity

---

- The space complexity of this approach is O(1).-

---

### One step at a time.
