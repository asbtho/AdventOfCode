def main():
    file = open(0).read().splitlines()
    part1(file)
    part2(file)

def part1(file):
    times = file[0].replace("Time:","").split()
    distances = file[1].replace("Distance:","").split()

    times = [int(x) for x in times]
    distances = [int(x) for x in distances]

    totalWaysToWin = []
    totalWaysToWinMultiplied = 1
    for t, time in enumerate(times):
        waysToWin = 0
        for i in range(time):
            ms = i+1
            thisDistance = ms * (time-ms)
            if thisDistance > distances[t]:
                waysToWin += 1
        totalWaysToWin.append(waysToWin)
        totalWaysToWinMultiplied *= waysToWin
    
    print(totalWaysToWin)
    print(totalWaysToWinMultiplied)


def part2(file):
    time = int("".join(file[0].replace("Time:","").split()))
    distance = int("".join(file[1].replace("Distance:","").split()))

    totalWaysToWinMultiplied = 1

    waysToWin = 0
    for i in range(time):
        ms = i+1
        thisDistance = ms * (time-ms)
        if thisDistance > distance:
            waysToWin += 1
    totalWaysToWinMultiplied *= waysToWin
    
    print(totalWaysToWinMultiplied)


main()