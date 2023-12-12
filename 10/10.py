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

    directions = ((0,1),(1,0),(-1,0),(0,-1))
    results = []

    for dir in directions:
        count, result = startLoop(start,grid,dir)
        if result == 1:
            results.append((count, count/2, result, dir))
    
    print("Part 1: " + str(results))

    emptyGrid = paintLoop(start,grid,results[0][3],emptyGrid)
    emptyGrid, internalcount = checkInternal(emptyGrid)
    for r, row in enumerate(emptyGrid):
        print("".join(row))
    print("INTERNAL COUNT: " + str(internalcount))


def startLoop(start,grid,startDir):
    prevCoords = start
    nCoords = tuple(map(sum, zip(start,startDir)))
    count = 0
    while True:
        count += 1
        char = grid[nCoords[0]][nCoords[1]]
        print(char + " on coords: " + str(nCoords) + " on count: " + str(count))
        nCoords,prevCoords = tuple(map(sum, zip(nCoords,getNext(char,nCoords,prevCoords)))),nCoords
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
        nCoords,prevCoords = tuple(map(sum, zip(nCoords,getNext(char,nCoords,prevCoords)))),nCoords
        if char == "S":
            emptyGrid[nCoords[0]][nCoords[1]] = "F"
            break
    return emptyGrid

def checkInternal(emptyGrid):
    internalcount = 0
    for r, row in enumerate(emptyGrid):
        outside = True
        f_found = False
        l_found = False
        for c, ch in enumerate(row):
            if ch == "|":
                outside = not outside
            if ch == "7":
                if f_found:
                    f_found = False
                if l_found:
                    outside = not outside
                    l_found = False
            if ch == "F":
                f_found = True
            if ch == "L":
                l_found = True
            if ch == "J":
                if f_found:
                    outside = not outside
                    f_found = False
                if l_found:
                    l_found = False
            if ch == ".":
                if not outside:
                    internalcount += 1
                    emptyGrid[r][c] = "I"
                else:
                    emptyGrid[r][c] = "O"
    return emptyGrid, internalcount


def getNext(char,nCoords,prevCoords):
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