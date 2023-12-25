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

    total = 0

    for pattern in patterns:
        total += findReflection(pattern)

    print(total)


def findReflection(pattern):
    # Check edge cases, rows
    if diff(pattern[0],pattern[1]) == 1:
        return 1*100
    if diff(pattern[len(pattern)-2],pattern[len(pattern)-1]) == 1:
        return (len(pattern)-1)*100
    
    #Check edge cases, columns
    if diff(columnGet(pattern, 0), columnGet(pattern, 1)) == 1:
        return 1
    if diff(columnGet(pattern, len(pattern[0])-2), columnGet(pattern, len(pattern[0])-1)) == 1:
        return (len(pattern[0])-1)

    # Check rows
    for i in range(len(pattern)):
        if i > 0:
            if (pattern[i] == pattern[i-1]) or (diff(pattern[i],pattern[i-1]) == 1):
                if i <= len(pattern)/2:
                    rev = pattern[i:i+i]
                    rev.reverse()
                    if pattern[0:i] == rev:
                        continue
                    else:
                        list = diffList(pattern[0:i], rev)
                        if len(list) == 2:
                            if diff(list[0], list[1]) == 1:
                                return i*100
                else:
                    count = len(pattern)-i
                    rev = pattern[i-count:i]
                    rev.reverse()
                    if pattern[i:len(pattern)] == rev:
                        continue
                    else:
                        list = diffList(pattern[i:len(pattern)], rev)
                        if len(list) == 2:
                            if diff(list[0], list[1]) == 1:
                                return i*100
                    
    # Check vertical
    columns = []
    vertical = False 
    verticalCenters = [] 

    for i in range(len(pattern[0])):
        column = columnGet(pattern, i)
        columns.append(column)
        if i > 0:
            if column == columns[i-1] or diff(column, columns[i-1]) == 1:
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
                    continue
                else:
                    list = diffList(columns[0:i], rev)
                    if len(list) == 2:
                        if diff(list[0], list[1]) == 1:
                            verticalNumber = i
            else:
                count = len(columns)-i
                rev = columns[i-count:i]
                rev.reverse()
                if columns[i:len(columns)] == rev:
                    continue
                else:
                    list = diffList(columns[i:len(columns)], rev)
                    if len(list) == 2:
                        if diff(list[0], list[1]) == 1:
                            verticalNumber = i
    
    return verticalNumber


def diff(item1, item2):
    count = 0
    for i in range(len(item1)):
        if item1[i] != item2[i]:
            count += 1
    return count


def diffList(li1, li2):
    li_dif = []
    for i in range(len(li1)):
        if li1[i] != li2[i]:
            li_dif.append(li1[i])
            li_dif.append(li2[i])
    return li_dif


def columnGet(grid, i):
    return [row[i] for row in grid]


def rowGet(grid, i):
    return grid[i]


main()
