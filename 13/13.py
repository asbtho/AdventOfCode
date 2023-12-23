def main():
    lines = open(0).read().splitlines()

    patterns = []

    pattern = []
    for line in lines:
        if line == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)

    #print(patterns)

    total = 0

    for pattern in patterns:
        total += findReflection(pattern)

    print(total)


def findReflection(pattern):
    for i in range(len(pattern)):
        if i > 0:
            if pattern[i] == pattern[i-1]:
                if i <= len(pattern)/2:
                    rev = pattern[i:i+i]
                    rev.reverse()
                    if pattern[0:i] == rev:
                        return i*100
                else:
                    count = len(pattern)-i
                    rev = pattern[i-count:i]
                    rev.reverse()
                    if pattern[i:len(pattern)] == rev:
                        return i*100
                    
    # If not found horizontal reflection, check vertical
    columns = []
    vertical = False 
    verticalCenters = [] 

    for i in range(len(pattern[0])):
        column = columnGet(pattern, i)
        columns.append(column)
        if i > 0:
            if column == columns[i-1]:
                vertical = True
                verticalCenters.append((i-1, i))
    
    verticalNumber = 0
    if vertical:
        for verticalCenter in verticalCenters:
            i = verticalCenter[1]
            if i <= len(columns)/2:
                rev = columns[i:i+i]
                rev.reverse()
                if columns[0:i] == rev:
                    verticalNumber = i
            else:
                count = len(columns)-i
                rev = columns[i-count:i]
                rev.reverse()
                if columns[i:len(columns)] == rev:
                    verticalNumber = i
    
    if verticalNumber != 0:
        return verticalNumber


def columnGet(grid, i):
    return [row[i] for row in grid]


def rowGet(grid, i):
    return grid[i]


main()
