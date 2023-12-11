def main():
    grid = open(0).read().splitlines()
    emptyGrid = []

    start = (0,0)
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
    
    for r, row in enumerate(grid):
        rowinput = []
        for c, ch in enumerate(row):
            rowinput.append(".")
        emptyGrid.append(rowinput)
    #emptyGrid[start[0]][start[1]] = "S"

    directions = ((0,1),(1,0),(-1,0),(0,-1))
    results = []

    for dir in directions:
        count, result = startLoop(start,grid,dir)
        if result == 1:
            results.append((count, count/2, result, dir))
    
    print("Part 1: " + str(results))

    emptyGrid = paintLoop(start,grid,results[0][3],emptyGrid)
    for r, row in enumerate(emptyGrid):
        print("".join(row))


def startLoop(start,grid,startDir):
    prevCoords = start
    nCoords = tuple(map(sum, zip(start,startDir)))
    count = 0
    while True:
        count += 1
        char = grid[nCoords[0]][nCoords[1]]
        print(char + " on coords: " + str(nCoords) + " on count: " + str(count))
        nCoords,prevCoords = tuple(map(sum, zip(nCoords,getNextClockwise(char,nCoords,prevCoords)))),nCoords
        if char == "S":
            return count, 1
        if char == "." or nCoords == prevCoords:
            return count, -1
        

def paintLoop(start,grid,startDir,emptyGrid):
    prevCoords = start
    nCoords = tuple(map(sum, zip(start,startDir)))
    while True:
        char = grid[nCoords[0]][nCoords[1]]
        emptyGrid[nCoords[0]][nCoords[1]] = char
        nCoords,prevCoords = tuple(map(sum, zip(nCoords,getNextClockwise(char,nCoords,prevCoords)))),nCoords
        if char == "S":
            break
    return emptyGrid
    

def getNextClockwise(char,nCoords,prevCoords):
    if char == "|":
        if prevCoords[0] < nCoords[0]:
            return (1,0)
        elif prevCoords[0] > nCoords[0]:
            return (-1,0)
        else:
            return (0,0)
    elif char == "L":
        if prevCoords[1] > nCoords[1]:
            return (-1,0)
        elif prevCoords[0] < nCoords[0]:
            return (0,1)
        else:
            return (0,0)
    elif char == "J":
        if prevCoords[1] < nCoords[1]:
            return (-1,0)
        elif prevCoords[0] < nCoords[0]:
            return (0,-1)
        else:
            return (0,0)
    elif char == "7":
        if prevCoords[1] < nCoords[1]:
            return (1,0)
        elif prevCoords[0] > nCoords[0]:
            return (0,-1)
        else:
            return (0,0)
    elif char == "F":
        if prevCoords[1] > nCoords[1]:
            return (1,0)
        elif prevCoords[0] > nCoords[0]:
            return (0,1)
        else:
            return (0,0)
    elif char == "-":
        if prevCoords[1] > nCoords[1]:
            return (0,-1)
        elif prevCoords[1] < nCoords[1]:
            return (0,1)
        else:
            return (0,0)
    else:
        return (0,0)


main()