def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    if i == len(array)-1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i+1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# Solution 2

# def getPermutations(array):
#     permutations=[]
#     permutationsHelper(array,[],permutations)
#     return permutations

# def permutationsHelper(array,currentPermutation,permutations):
#     # print('out',len(array))
#     if not len(array) and len(currentPermutation):
#         # print('in',len(array))
#         # print(currentPermutation)
#         permutations.append(currentPermutation)
#     else:
#         for i in range(len(array)):
#             newArray=array[:i]+array[i+1:]
#             newPermutation=currentPermutation+[array[i]]
#             # print(newPermutation)
#             permutationsHelper(newArray,newPermutation,permutations)

#     # Write your code here.
#     pass
