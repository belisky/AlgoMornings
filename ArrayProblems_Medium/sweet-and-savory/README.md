# Sweet and Savory...
![sweet-or-savory](https://github.com/belisky/AlgoMornings/assets/61013338/b0362394-1667-4028-bdda-28fe127f3eb0)


- ## **_Category-Arrays_**
- ### **_Difficulty-Medium_**

You're given an array of dishes and a target combined flavor profile. Write a function that return the best possible pairing of two dishes (the pairing with a total flavor profile that's closes to the target). Note that the pairing must include one sweet and one savory dish. You're also concerned about the dish being too savory, so your pairing shuold never be more savory than the target flavor profile.

## Sample Input

---

dishes=[-3,-5,1,7]
target=8

## Sample Output

---

[-3,7]

## Approach to Solution

---

- I separate the dishes into sweet and savory, sorted in ascending order.
- with pointers on both separated dishes, I try to combine them to get the best effect and adjust the pointers appropriately in that regard.
- I then check if each combination is closer to the target as possible and return the best possible combination.

### Time Complexity

---

-The time complexity of this approach is O(nlog(n)).

### Space Complexity

---

-The space complexity of this approach is O(n)
where n is the length of the dishes

---

### One step at a time.
