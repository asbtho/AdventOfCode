from math import gcd
def main():
    file = open(0).read().splitlines()

    instructions = file[0]
    maps = createMapsDict(file)
    #part1(maps,instructions)
    part2(maps,instructions)

def part2(maps,instructions):
    starts = []
    for map in maps:
        if map[2] == "A":
            starts.append(map)

    intervals = []

    for start in starts:
        curKey = start
        steps = 0
        rounds = 500
        lastStep = 0
        while (not rounds <= 0):
            for dir in instructions:
                curKey = getNextMap(maps,curKey,dir)
                steps += 1
                if curKey[2] == "Z":
                    interval = steps - lastStep
                    lastStep = steps
            rounds -= 1
        intervals.append(interval)
                    
    lcm = 1
    for i in intervals:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)
    print(intervals)


def part1(maps,instructions):
    start = "AAA"
    end = "ZZZ"
    curKey = start
    steps = 0
    while (not curKey == end):
        for dir in instructions:
            curKey = getNextMap(maps,curKey,dir)
            steps += 1
            if curKey == end:
                break
    print(steps)

def createMapsDict(file):
    maps = {}
    for line in file:
        if "=" in line:
            key, map = line.split(" = ")
            map = map.replace("(","").replace(")","").split(", ")
            maps[key] = map
    return maps


def getNextMap(maps,key,dir):
    if dir == "L":
        return maps[key][0]
    elif dir == "R":
        return maps[key][1]
    else:
        print("ERROR")
        return -1


main()