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


def myLargestRectangleUnderSkyline(buildings):
    pillarIndices = []
    maxArea = 0
    for idx, height in enumerate(buildings + [0]):
        while len(pillarIndices) != 0 and buildings[pillarIndices[-1]] >= height:
            lastHighestIdx = pillarIndices.pop()
            pillarHeight = buildings[lastHighestIdx]
            width = idx if len(pillarIndices) == 0 else idx - pillarIndices[-1] - 1
            maxArea = max(width * pillarHeight, maxArea)
        pillarIndices.append(idx)
    print(maxArea)


input_buildings_3 = [2, 1, 2]
largestRectangleUnderSkyline(input_buildings_3)

input_buildings_3 = [2, 1]
largestRectangleUnderSkyline(input_buildings_3)

# maxArea should be 6 instead of 4
input_buildings_3 = [1, 4, 3, 1]
largestRectangleUnderSkyline(input_buildings_3)
myLargestRectangleUnderSkyline(input_buildings_3)
