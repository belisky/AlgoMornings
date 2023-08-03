# Minimum Number of Jumps...
![min-jumps](https://github.com/belisky/AlgoMornings/assets/61013338/dfbbf091-3c0f-4d4c-ac9a-4e0a064e519c)


- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

You're given a non-empty array of positive integers where each integer represents the maximum number os steps you can take forward in the array. For example, if the element at index 1 is 3, you can go from index 1 to index 2,3,4.

Write a function that returns the minimum number of jumps needed to reach the final index.

Note that jumping from index i to index i+x always constitures one jump, no matter how large x is.

## Sample Input

---

array=[3,4,2,1,2,3,7,1,1,1,3]

## Sample Output

---

4

## Approach to Solution

---

- I create a jumps array that stores the minimum number of jumps required to get to a particular index.
- I loop through the array and at each index, I loop through the array from the beginning of the array to that index(inner for loop).
- I check if I can jump from my current position in the inner array to surpass the index of the outer array.

```
   for i in range(1,len(array)):
        for j in range(0,i):
            if array[j]+j>=i:
                jumps[i]=min(jumps[j]+1,jumps[i])
```

- I return the last element of the array as answer.

### Time Complexity

---

- The time complexity of this approach is O(n^2)

### Space Complexity

---

- The space complexity of this approach is O(n).

### One step at a time.
