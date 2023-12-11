import time
def main():
    startTime = time.time()
    file = open(0).read().splitlines()
    seeds = []
    seedtosoilarr = []
    soiltofertarr = []
    ferttowaterarr = []
    watertolightarr = []
    lighttotemparr = []
    temptohumarr = []
    humtolocarr = []
    seedtosoil = False
    soiltofert = False
    ferttowater = False
    watertolight = False
    lighttotemp = False
    temptohum = False
    humtoloc = False

    for line in file:
        if "seeds: " in line:
            seeds = line.split(" ")
            seeds.remove("seeds:")
        if line in ['\n', '\r\n', '']:
            seedtosoil = False
            soiltofert = False
            ferttowater = False
            watertolight = False
            lighttotemp = False
            temptohum = False
            humtoloc = False
        if(seedtosoil):
            seedtosoilarr.append(line.split(" "))
        if(soiltofert):
            soiltofertarr.append(line.split(" "))
        if(ferttowater):
            ferttowaterarr.append(line.split(" "))
        if(watertolight):
            watertolightarr.append(line.split(" "))
        if(lighttotemp):
            lighttotemparr.append(line.split(" "))
        if(temptohum):
            temptohumarr.append(line.split(" "))
        if(humtoloc):
            humtolocarr.append(line.split(" "))
        
        if "seed-to-soil map:" in line:
            seedtosoil = True
            continue
        if "soil-to-fertilizer map:" in line:
            soiltofert = True
            continue
        if "fertilizer-to-water map:" in line:
            ferttowater = True
            continue
        if "water-to-light map:" in line:
            watertolight = True
            continue
        if "light-to-temperature map:" in line:
            lighttotemp = True
            continue
        if "temperature-to-humidity map:" in line:
            temptohum = True
            continue
        if "humidity-to-location map:" in line:
            humtoloc = True
            continue
    
    firstLocationFound = False
    finalLocationFound = False
    loc = 0
    nextSeed = 0
    while not finalLocationFound:
        if (firstLocationFound):
            loc += 1
        else:
            loc += 100000
        #print(loc)
        for arr in humtolocarr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if loc + diff >= int(arr[1]) and loc + diff <= max:
                nextSeed = loc + diff
                break
            nextSeed = loc
        for arr in temptohumarr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if nextSeed + diff >= int(arr[1]) and nextSeed + diff <= max:
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in lighttotemparr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if nextSeed + diff >= int(arr[1]) and nextSeed + diff <= max:
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in watertolightarr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if nextSeed + diff >= int(arr[1]) and nextSeed + diff <= max:
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in ferttowaterarr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if nextSeed + diff >= int(arr[1]) and nextSeed + diff <= max:
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in soiltofertarr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if nextSeed + diff >= int(arr[1]) and nextSeed + diff <= max:
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in seedtosoilarr:
            max = int(arr[1]) + int(arr[2])
            diff = int(arr[1]) - int(arr[0])
            if nextSeed + diff >= int(arr[1]) and nextSeed + diff <= max:
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for i, seed in enumerate(seeds):
            if (i % 2) == 0:
                startSeed = int(seed)
                endSeed = startSeed + int(seeds[i+1])
                if nextSeed >= startSeed and nextSeed <= endSeed:
                    print("FOUND: " + str(nextSeed))
                    if(firstLocationFound):
                        finalLocationFound = True
                    firstLocationFound = True
                    if(finalLocationFound):
                        continue
                    else:
                        loc -= 100000
                else:
                    print(str(nextSeed) + " NOT IN RANGE OF " + str(startSeed) + "-" + str(endSeed))
            else:
                continue

    executionTime = (time.time() - startTime)
    print("FINAL: " + str(loc))
    print('PART 2 Execution time in seconds: ' + str(executionTime))

main()