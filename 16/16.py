def main():
    map = open(0).read().splitlines()

    emptyMap = createEmptyMap(map)

    queue = [(0,0,"right")]

    for line in emptyMap:
        print(line)



def createEmptyMap(map):
    newMap = []
    for line in map:
        newMap.append("."*len(line))
    return newMap


def checkTile(map, direction, this):
    dirC = {
        "right": (0,1),
        "down": (1,0),
        "left": (0,-1),
        "up": (-1,0),
        "left_right": ((0,-1),(0,1)),
        "up_down": ((-1,0),(1,0))
    }

    yC, xC = this[0], this[1]
    tile = map[yC][xC]

    if tile == ".":
        return dirC[direction]
    
    if tile == "/":
        if direction == "right":
            return dirC["up"]
        elif direction == "down":
            return dirC["left"]
        elif direction == "left":
            return dirC["down"]
        else:
            return dirC["right"]
        
    if tile == "|":
        if direction == "down" or direction == "up":
            return dirC[direction]
        else:
            return dirC["left_right"]
    
    if tile == "-":
        if direction == "left" or direction == "right":
            return dirC[direction]
        else:
            return dirC["up_down"]



main()