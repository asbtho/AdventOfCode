def main():
    grid = open(0).read().splitlines()
    coords = getGalaxyCoords(grid)
    rows,columns = expandRows(grid),expandColumns(grid)
    coords = expandCoords(coords,rows,columns)
    calculateAllDistances(coords)


def columnGet(grid, i):
    return [row[i] for row in grid]


def rowGet(grid, i):
    return grid[i]


def expandCoords(coords,rows,columns):
    for galaxy, coord in coords.items():
        xToAdd,yToAdd = 0,0
        for y in rows:
            if coord[0] > y:
                yToAdd += 1000000-1
        for x in columns:
            if coord[1] > x:
                xToAdd += 1000000-1
        coord[0] += yToAdd
        coord[1] += xToAdd
    return coords


def expandRows(grid):
    i = 0
    rowList = []
    while i < len(grid):
        if "#" in rowGet(grid, i):
            i += 1
        else:
            rowList.append(i)
            i += 1
    return rowList


def expandColumns(grid):
    i = 0
    columnList = []
    while i < len(grid[0]):
        if "#" in columnGet(grid, i):
            i += 1
        else:
            columnList.append(i)
            i += 1
    return columnList


def getGalaxyCoords(grid):
    coords = {}
    count = 1
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                coords[count] = [r,c]
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
