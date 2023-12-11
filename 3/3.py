def main():
    file = open('input.txt','r')
    array = createArray(file)
    parts = findPartNumbers(array)
    gears = findGears(array)
    print("PARTS: " + str(parts))
    print("GEARS: " + str(gears))
                
# PART 1
def findPartNumbers(array):
    total = 0
    for y, line in enumerate(array):
        foundDigit = False
        for x, char in enumerate(line):
            if char.isdigit() and (not foundDigit):
                foundDigit = True
                digitLength = 1
                number = "" + char
                if x == len(line)-1:
                    foundDigit = False
                    total += checkForChars(x,y,digitLength-1,array,number)
            elif char.isdigit() and foundDigit:
                digitLength += 1
                number += char
                if x == len(line)-1:
                    foundDigit = False
                    total += checkForChars(x,y,digitLength-1,array,number)
            elif (not char.isdigit()) and (not foundDigit):
                continue
            else:
                foundDigit = False
                total += checkForChars(x,y,digitLength,array,number)
    return total

# PART 2
def findGears(array):
    sumRatios = 0
    for y, line in enumerate(array):
        for x, char in enumerate(line):
            if char == "*":
                gearNumbers = []
                xStart = x-3
                if (not y-1 < 0):
                    gearNumbers.extend(getGearNumbers(array,line,xStart,y-1,x))
                if (not y+1 > len(array)-1):
                    gearNumbers.extend(getGearNumbers(array,line,xStart,y+1,x))
                gearNumbers.extend(getGearNumbers(array,line,xStart,y,x))
                if len(gearNumbers) == 2:
                    sumRatios += int(gearNumbers[0])*int(gearNumbers[1])
    return sumRatios


def getGearNumbers(array,line,xStart,yValue,x):
    creatingNumber = ""
    foundDigit = False
    digitConnected = False
    tempArray = []
    for i in range(7):
        if (not xStart+i < 0) and (not xStart+i > len(line)-1):
            if array[yValue][xStart+i].isdigit() and (not foundDigit):
                foundDigit = True
                if xStart+i == x-1 or xStart+i == x+1 or xStart+1 == x:
                    digitConnected = True
                creatingNumber += array[yValue][xStart+i]
            elif array[yValue][xStart+i].isdigit() and foundDigit:
                creatingNumber += array[yValue][xStart+i]
                if xStart+i == x-1 or xStart+i == x+1 or xStart+1 == x:
                    digitConnected = True
            else:
                foundDigit = False
                if len(creatingNumber) > 0 and digitConnected:
                    tempArray.append(creatingNumber)
                    digitConnected = False
                creatingNumber = ""
    if(foundDigit):
        foundDigit = False
        if len(creatingNumber) > 0 and digitConnected:
            tempArray.append(creatingNumber)
            digitConnected = False
        creatingNumber = ""
    return tempArray


def createArray(file):
    array = []
    for line in file:
        array.append(line.replace('\n',''))
    return array


def checkForChars(x,y,digitLength,array,number):
    checkLength = digitLength + 1
    for i in range(checkLength+1):
        if (not x-i < 0):
            if (not array[y][x-i].isdigit()) and array[y][x-i] != ".":
                return int(number)
        if (not y-1 < 0):
            if (not array[y-1][x-i].isdigit()) and array[y-1][x-i] != ".":
                return int(number)
        if (not y+1 > len(array)-1):                 
            if (not array[y+1][x-i].isdigit()) and array[y+1][x-i] != ".":
                return int(number)
    return 0


main()