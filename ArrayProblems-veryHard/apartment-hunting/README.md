# Apartment Hunting...

- ## **_Category-Arrays_**
- ### **_Difficulty-veryHard_**

![apartment-hunting](https://github.com/belisky/AlgoMornings/assets/61013338/acb6ced9-cd7c-4210-8a96-724c29377489)


You're looking to move into a new apartment on specific street. You also have a list of requirements. For instance you might value having a school and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that are preent and absent at the block in question.

In order to make your life easy, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.

Write a function that takes in a lit of contiguous blocks ona specific street and a list of your required buildings that returns the location(index) of the block that's most optimal.

## Sample Input

---

blocks = [

{
"gym":false,
"school":true,
"store":false
},

{
"gym":true,
"school":false,
"store":false
},

{
"gym":true,
"school":true,
"store":false
},

{
"gym":false,
"school":true,
"store":false
},

{
"gym":false,
"school":true,
"store":true
}
]

reqs=["gym","school","store"]

## Sample Output

3

## Approach to Solution

---

- I loop through the whole blocks array first from left-to-right and then from right-to-left.

From left to right.

- At every particular block I loop through the reqs to see if that req is available(true) on that block.
- if the req is true on that block, I initialize its value to 0 in an array of dictionaries I have already instantiated.
- else if the req is false, I set the dictionary value to the previous reqs value+1

From right to left.

- At every particular block I loop through the reqs to see if that req is available(true) on that block.
- if the req is true on that block, I initialize its value to 0 in an array of dictionaries I have already instantiated.
- else if the req is false, I set the dictionary value to the min(previous reqs value+1,current req value).

I finally loop through the array of dictionaries to find the index of the most suitable block.

### Time Complexity

---

- The time complexity of this approach is O(mn).
  Where m is the number of blocks and n is the number of reqs(requirements)

### Space Complexity

- The space complexity is also O(mn).

---

-The space complexity of this approach is O(n)
where n is the length of the hashmap and the quadruplets array.

---

### One step at a time.
