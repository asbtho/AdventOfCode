def main():
    platform = open(0).read().splitlines()
    #part1(platform)
    part2(platform)
    

def part2(platform):
    cache = {}
    cycleCache = []
    cycleLength = 0
    for i in range(1000000000):
        key = ",".join(platform)

        if key in cache:
            if cache[key] in cycleCache:
                break
            else:
                cycleLength += 1
                cycleCache.append(cache[key])
        else:
            cache[key] = i

        platform = tilt(platform)
        for j in range(3):
            platform = rotateClockWise(platform)
            platform = tilt(platform)
        platform = rotateClockWise(platform)

    value = (1000000000 - cycleCache[0]) % cycleLength
    cachedplatform = list(cache)[cycleCache[value]].split(",")
    
    count = calcLoad(cachedplatform)
    print(count)


def part1(platform):
    endplatform = tilt(platform)
    count = calcLoad(endplatform)
    print(count)


def tilt(platform):
    hit = True
    while(hit):
        hit=False
        for i, line in reversed(list(enumerate(platform))):
            if i == 0:
                continue
            for j, char in enumerate(line):
                if char == "O":
                    if platform[i-1][j] == ".":
                        hit = True
                        platform[i] = platform[i][:j] + "." + platform[i][j+1:]
                        platform[i-1] = platform[i-1][:j] + "O" + platform[i-1][j+1:]
    return platform


def rotateClockWise(platform):
    rotated = [list(reversed(col)) for col in zip(*platform)]
    rotated = ["".join(line) for line in rotated]
    return rotated


def calcLoad(platform):
    count, i = 0, len(platform)
    for line in platform:
        for char in line:
            if char == "O":
                count += i
        i -= 1
    return count


main()