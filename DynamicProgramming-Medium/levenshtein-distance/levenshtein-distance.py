def levenshteinDistance(str1, str2):
    edits_table=[[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for row in range(len(str2)+1):
        edits_table[row][0]=row
    for row in range(1,len(str2)+1):
        for col in range(1,len(str1)+1):
            if str1[col-1]==str2[row-1]:
                edits_table[row][col]=edits_table[row-1][col-1]
            else:
                edits_table[row][col]=1+min(edits_table[row-1][col],edits_table[row][col-1],edits_table[row-1][col-1])
    return edits_table[-1][-1]
            