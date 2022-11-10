def largestRectangleUnderSkyline(buildings):
    pillarIndices = []
    maxArea = 0
    for idx, height in enumerate(buildings + [0]):
        while len(pillarIndices) != 0 and buildings[pillarIndices[-1]] > height:
            lastHighestIdx = pillarIndices.pop()
            pillarHeight = buildings[lastHighestIdx]
            width = idx if len(pillarIndices) == 0 else idx - lastHighestIdx
            maxArea = max(width * pillarHeight, maxArea)
        pillarIndices.append(idx)
    print(maxArea)


input_buildings = [2, 1, 2]
largestRectangleUnderSkyline(input_buildings)
