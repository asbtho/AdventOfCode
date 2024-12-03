def main():
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
    locationNumbers = []

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
    
    for seed in seeds:
        nextSeed = 0
        originalSeed = int(seed)
        for arr in seedtosoilarr:
            max = int(arr[1]) + int(arr[2])
            if originalSeed >= int(arr[1]) and originalSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = originalSeed + diff
                break
            nextSeed = originalSeed
        for arr in soiltofertarr:
            max = int(arr[1]) + int(arr[2])
            if nextSeed >= int(arr[1]) and nextSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in ferttowaterarr:
            max = int(arr[1]) + int(arr[2])
            if nextSeed >= int(arr[1]) and nextSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in watertolightarr:
            max = int(arr[1]) + int(arr[2])
            if nextSeed >= int(arr[1]) and nextSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in lighttotemparr:
            max = int(arr[1]) + int(arr[2])
            if nextSeed >= int(arr[1]) and nextSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in temptohumarr:
            max = int(arr[1]) + int(arr[2])
            if nextSeed >= int(arr[1]) and nextSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        for arr in humtolocarr:
            max = int(arr[1]) + int(arr[2])
            if nextSeed >= int(arr[1]) and nextSeed <= max:
                diff = int(arr[0]) - int(arr[1])
                nextSeed = nextSeed + diff
                break
            nextSeed = nextSeed
        seedMap = [originalSeed,nextSeed]
        locationNumbers.append(seedMap)

    print(locationNumbers)
    lowestNumber = locationNumbers[0][1]
    for loc in locationNumbers:
        if loc[1] < lowestNumber:
            lowestNumber = loc[1]
    print(lowestNumber)



main()