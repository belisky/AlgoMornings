# Numbers in pi...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

Given a string representation of the first n digits of Pi and a list of positive integers(all in string format), write a function that returns the smallest number of spaces that can be added to the n digits of Pi such taht all resulting nubers are found in the list of integers.

## Sample Input

---

pi="3141592653589793238462643383279"
numbers=["314159265358979323846","26433","8","3279","314159265","31415926535897932384626433832","79"]

## Sample Output

---

48

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n^3+m) where n is the number of digits in Pi and is the number of favorite numbers

### Space Complexity

---

- The space complexity of this approach is O(n+m)

### One step at a time.
