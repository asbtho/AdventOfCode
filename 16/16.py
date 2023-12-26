def main():
    map = open(0).read().splitlines()

    emptyMap = createEmptyMap(map)

    for line in emptyMap:
        print(line)



def createEmptyMap(map):
    newMap = []
    for line in map:
        newMap.append("."*len(line))
    return newMap


def checkTile(map, this, next):
    print("START")


main()