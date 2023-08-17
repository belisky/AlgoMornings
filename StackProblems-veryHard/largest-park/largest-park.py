def largestPark(land):
    heights = [0] * len(land[0])
    maxArea = 0

    for row in land:
        for colIndex in range(len(land[0])):
            heights[colIndex] = heights[colIndex] + \
                1 if row[colIndex] == False else 0
        maxArea = max(maxArea, largestRectangleHistogram(heights))
    return maxArea


def largestRectangleHistogram(heights):
    stack = []
    maxArea = 0

    for colIndex in range(len(heights)):
        while len(stack) > 0 and heights[colIndex] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = colIndex if len(stack) == 0 else colIndex-stack[-1]-1
            maxArea = max(maxArea, width*height)
        stack.append(colIndex)
    while len(stack) > 0:
        height = heights[stack.pop()]
        width = len(heights) if len(stack) == 0 else len(heights)-stack[-1]-1
        maxArea = max(maxArea, width*height)
    return maxArea

    # Write your code here.
