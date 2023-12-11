def main():
    file = open('input.txt','r')
    total = 0
    for line in file:
        game = line.split(": ", 1)[0]
        sets = line.split(": ", 1)[1].split("; ")
        print(game)
        gamePossible = True
        minimumRed = 0
        minimumBlue = 0
        minimumGreen = 0
        for set in sets:
            print(set)
            cubes = set.split(", ")
            for cube in cubes:
                number = int(cube.split(" ", 1)[0])
                color = cube.split(" ", 1)[1]
                color = color.replace("\n","")
                if color == "green":
                    if number > minimumGreen:
                        minimumGreen = number
                elif color == "blue":
                    if number > minimumBlue:
                        minimumBlue = number
                elif color == "red":
                    if number > minimumRed:
                        minimumRed = number
        print("RED: " + str(minimumRed) + " BLUE: " + str(minimumBlue) + " GREEN: " + str(minimumGreen))
        powerOf = minimumRed * minimumBlue * minimumGreen
        print(powerOf)
        total += powerOf
    return total

print(main())