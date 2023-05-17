# Calendar Matching...

- ## **_Category-Arrays_**
- ### **_Difficulty-veryHard_**

Write a function that takes in your calendar, you daily bounds, your co-worker's calendar and their daily bounds and the duration of the meeting you want to schedule, and that returns a list of all the time blocks during which you could schedule the meeting ordered from earlies time block to latest.

## Sample Input

---

calendar1=[['9:00','10:30'],['12:00':'13:00'],['16:00','18:00']]

dailyBounds1=['9:00','20:00']
calendar2=[['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
dailyBounds2=['10:00','18:30']
meetingDuration=30

## Sample Output

[['11:30','12:00'],['15:00','16:00'],['18:00','18:30']]

## Approach to Solution

---

- I first find the dailyBounds common to the two parties.
- I use the common dailyBounds to get the freetimes of both parties
- I then use the freeTimes of both parties to find the overlapping freeTimes that are at least the meetingDuration.
- I return the Overlapping freeTimes in an array format like the calendars

### Time Complexity

---

- The time complexity of this approach is O(a1+b1).
  Where a1 and b1 is the number of meetings in calendar1 and calendar2.

### Space Complexity

- The space complexity is also O(a1+b2).

---

### One step at a time.
