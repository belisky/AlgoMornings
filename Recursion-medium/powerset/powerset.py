def powerset(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset+[element])
            # print(currentSubset+[element])
    return subsets
