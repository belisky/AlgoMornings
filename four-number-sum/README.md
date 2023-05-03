# Four-Number-Sum...

This is a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function finds all quadruplets in the array that sum up to the target sum and returns a two-dimensional array of all those quadruplets

## Sample Input

---

array=[7,6,4,-1,1,2]
targetSum=16

## Sample Output

---

[[7,6,4,-1],[7,6,1,2]]

## Approach to Solution

---

-I loop through the whole array using pointer i
-At every particular element that i points to, I loop through from the beginning of the original array to i using pointer k;
ie: initialSum=array[k]+array[i], which is stored in a hashtable.

- I also loop through from i to the end of the array using pointer j;
  ie: secondSum=array[i]+array[j]
- If targetSum-initialSum=secondSum,
  then i append the elements of secondSum and initialSum to a quadruplets array.
- I return the quadruplets array at the end of i's loop.

### Time Complexity

---

-The time complexity of this approach is O(n\*\*2).
ie: for loop for i,
for loop for j:
etc.
for loop for k:
etc.

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the hashmap and the quadruplets array.

### One step at a time.
