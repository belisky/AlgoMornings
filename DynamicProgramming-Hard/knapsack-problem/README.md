# knapSack Problem...

- ## **_Category-Dynamic Programming_**
- ### **_Difficulty-Hard_**

You're given an array of arrays where each subarray hold two integer values and represents an item; the first integer is the item's value, and the second integer is the item's weight. You're also given an integer representing the maximum capacity of a knapsack that you have.

Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity, all the while maximizing their combined value. NOte that you only have one each item at your disposal.

Write a function that returns the maximized combined value of the items that you should pick as well as an array of the indices of each item picked.

## Sample Input

---

items=[[1,2],[4,3],[5,6],[6,7]]
capacity=10

## Sample Output

---

[10,[1,3]] // items [4,3] and [6,7]

## Approach to Solution

---

- I create a 2D array called knapSackValues.

```
knapSackValues=[[0 for x in range(0,capacity+1)] for y in range(0,len(items)+1)]


```

- I loop through the items input array using itemIdx.
- At each itemIdx, i loop through the range of the capacity given to see if my itemCapacity is less than or greater than the capacity

```
 for itemIdx in range(1,len(items)+1):
        curWeight=items[itemIdx-1][1]
        curValue=items[itemIdx-1][0]
        for capa in range(0,capacity+1):
            if curWeight>capa:
                knapSackValues[itemIdx][capa]=knapSackValues[itemIdx-1][capa]
            else:
                knapSackValues[itemIdx][capa]=max(knapSackValues[itemIdx-1][capa],knapSackValues[itemIdx-1][capa-curWeight]+curValue)
    return [knapSackValues[-1][-1],getKnapSackItems(knapSackValues,items)]

```

- I return the last item in the lcs array as an answer.

- To get the indices of the items in the knapSack, I back track throught the knapSackValues array with the condition that if the value at the current column is the same as the value in the column above, then the current item was not included in the items ...

```
def getKnapSackItems(knapSackValues,items):
    seq=[]
    itemSize=len(knapSackValues)-1
    col=len(knapSackValues[0])-1
    while itemSize>0:
        if knapSackValues[itemSize][col]==knapSackValues[itemSize-1][col]:
            itemSize-=1
        else:
            # print(i,i-1)
            seq.append(itemSize-1)
            col-=items[itemSize-1][1]
            itemSize-=1
        if col==0:
            break
    return list(reversed(seq))
```

NB: itemSize-1 to cater for 1 indexing instead of 0 indexing.

### Time Complexity

---

- The time complexity of this approach is O(n\*c)- where n is the number of items and c is the capacity.

### Space Complexity

---

- The space complexity of this approach is O(n\*c)- where n is the number of items and c is the capacity.

### One step at a time.
