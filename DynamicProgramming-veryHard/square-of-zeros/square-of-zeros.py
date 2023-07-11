def squareOfZeroes(matrix):
    n = len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            squareLen = 2
            while squareLen <= n-leftCol and squareLen <= n-topRow:
                bottomRow = topRow+squareLen-1
                rightCol = leftCol+squareLen-1
                if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
                    return True
                squareLen += 1
    return False


def isSquareOfZeroes(mat, tr, lc, br, rc):
    for row in range(tr, br+1):
        if mat[row][lc] != 0 or mat[row][rc] != 0:
            return False
    for col in range(lc, rc+1):
        if mat[tr][col] != 0 or mat[br][col] != 0:
            return False
    return True

    # Write your code here.
