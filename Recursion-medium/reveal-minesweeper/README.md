# Reveal Minesweeper...

- ## **_Category-Recursion_**
- ### **_Difficulty-medium_**

You're given a two-dimensional array of string that represents a Minesweeper board for a game in progress. You're also given a row and a colum representing the indices of the next square that the player clicks on the board. Write a function that returns an updated board after the click( your function can mutate teh input board).

if a player clicks on a mine, replace the 'M' with 'X', indicating the game was lost. 

If the player clicks on a cell adjacent to a mine, replace the 'H' with a string representing the number of adjacent mines...

## Sample Input

---

```
board=[
    ['M','H'],
    ['H','H'],
    ['H','H']
]
row=2
column=0

```

## Sample Output

---

```
[
    ['M','M'],
    ['2'.'2'],
    ['0','0']
]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(w\*h) time.- where w is the width of the board, and h is the height of the board.

### Space Complexity

---

- The space complexity of this approach is O(w\*h) space.

---

### One step at a time.
