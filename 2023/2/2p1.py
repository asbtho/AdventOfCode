def main():
    file = open('input.txt','r')
    total = 0
    for line in file:
        game = line.split(": ", 1)[0]
        sets = line.split(": ", 1)[1].split("; ")
        print(game)
        gamePossible = True
        for set in sets:
            cubes = set.split(", ")
            for cube in cubes:
                number = int(cube.split(" ", 1)[0])
                color = cube.split(" ", 1)[1]
                if (number > 12 and color == "red") or (number > 13 and color == "green") or (number > 14 and color == "blue"):
                    gamePossible = False
        if gamePossible:
            gameId = game.split(" ")[1]
            total += int(gameId)
    
    return total

print(main())