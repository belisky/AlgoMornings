# Power Number Mnemonics...

- ## **_Category-Recursion_**
- ### **_Difficulty-medium_**

 ----- ----- -----
|     |     |     |
|  1  |  2  |  3  |
|     | abc | def |
 ----- ----- -----
|     |     |     |
|  4  |  5  |  6  |
| ghi | jkl | mno |
 ----- ----- -----
|     |     |     |
|  7  |  8  |  9  |
| pqrs| tuv | wxyz|
 ----- ----- -----
      |     |     
      |  0  |     
      |     |    
       ----- 

Given a stringified phone number of any non-zero length, write a function that returnss all mnemonics for this phone number, in any order.

for this problem a valid mnemonic may onlly contain letters and the diggits `0` and `1`.


## Sample Input

---

```
phoneNumber='1905'
```

## Sample Output

---

```
 [
    '1w0j',
    '1w0k',
    '1w0l',
    '1x0j',
    '1x0k',
    '1y0j',
    '1y0k',
    '1y0l',
    '1z0j',
    '1z0k',
    '1z0l'
 ]
```

## Approach to Solution

---

### Time Complexity

---

- The time complexity of this approach is O(n\*4^n) time.-where n is the length of the input array.

### Space Complexity

---

- The space complexity of this approach is O(n\*4^n) space.

---

### One step at a time.
