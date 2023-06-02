# Tournament-Winner...

- ## **_Category-Arrays_**
- ### **_Difficulty-Easy_**
  Given an array of pairs representing the teams that have competed against each other and an array containing the result of each competition, write a function that returns the winner of the tournament. The input arrays are named _competitions_ and _results_.
  The _competitions_ array is of the form [hometeam,awayteam]. The _results_ array contains the corresponding winner of each competition, where 1 means the home team won and 0 means the away team won.

## Sample Input

---

competitions=[
['HTML','CSS'],
['CSS','PYTHON'],
['PYTHON','HTML']
]
results=[0,0,1]

## Sample Output

---

'PYTHON'

## Approach to Solution

---

- I loop through the Competitions array.
- At every particular competition, i update a score dictionary with the current winner.
- I check if the current winner's score is more than the current best team's score which is previously set to an empty string with score 0.
- if the current winnner's score is more than the current best, I update the current winner to be the current best.
- At the end of the loop, i just return the current best.

### Time Complexity

---

-The time complexity of this approach is O(n).

### Space Complexity

---

-The space complexity of this approach is O(m)
where m is the number of teams;

---

### One step at a time.
