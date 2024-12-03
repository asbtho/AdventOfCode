def main():
    grid = open(0).read().splitlines()

    grid = expandRows(grid)
    grid = expandColumns(grid)
    coords = getGalaxyCoords(grid)
    calculateAllDistances(coords)


def columnGet(grid, i):
    return [row[i] for row in grid]


def rowGet(grid, i):
    return grid[i]


def insertSpaceColumn(grid, i):
    grid = [row[:i]+"."+row[i:] for row in grid]
    return grid


def insertSpaceRow(grid, i):
    grid.insert(i,"." * len(grid[i]))
    return grid


def expandRows(grid):
    i = 0
    while i < len(grid):
        if "#" in rowGet(grid, i):
            i += 1
        else:
            grid = insertSpaceRow(grid, i)
            i += 2
    return grid


def expandColumns(grid):
    i = 0
    while i < len(grid[0]):
        if "#" in columnGet(grid, i):
            i += 1
        else:
            grid = insertSpaceColumn(grid, i)
            i += 2
    return grid


def getGalaxyCoords(grid):
    coords = {}
    count = 1
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                coords[count] = (r,c)
                count += 1
    return coords

def distance(coord1,coord2):
    return abs(coord1[1] - coord2[1]) + abs(coord1[0] - coord2[0])


def calculateAllDistances(coords):
    totalValue = 0
    for galaxy1, coord1 in coords.items():
        for galaxy2, coord2 in coords.items():
            if galaxy1 <= galaxy2:
                continue
            else:
                dist = distance(coord1,coord2)
                totalValue += dist
    print(totalValue)


main()
