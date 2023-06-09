# Majority Element...
![majority-element](https://github.com/belisky/AlgoMornings/assets/61013338/386e89f1-6ee7-4a6c-8f3d-d7b4ac086b8f)


- ## **_Category-Arrays_**
- ### **_Difficulty-Medium_**

You're given an unordered array of positive integers. A majority element is an element of the array that exits in over half of the indices. Write a function that takes in this array and returns the majority element.

## Sample Input

---

array=[1,2,3,2,2,1,2]

## Sample Output

---

2

## Approach to Solution

---

- I loop throught the whole array, and if my count is 0 the majority element is the current element in my iteration.
- if my count is not 0 and the current element is not the same as the majority element, I decrement count.
- if my count is still not 0 and the current element is the same as the majority element I increment count by 1.
- At the end of it all the number with most occurances will prevail as the majorityElementValue.

### Time Complexity

---

-The time complexity of this approach is O(n).

### Space Complexity

---

## -The space complexity of this approach is O(1)

### One step at a time.
