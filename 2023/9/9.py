def main():
    file = open(0).read().splitlines()
    numlist = createNumberedList(file)
    print(numlist)
    part1and2(numlist)

    
def part1and2(list):
    part1totalValue = 0
    part2totalValue = 0
    for seq in list:
        part1value = seq[-1]
        part2values = [seq[0]]
        nextSeq = seq
        while True:
            nextSeq, isZeroes = getNextSeq(nextSeq)
            part1value += nextSeq[-1]
            part2values.append(nextSeq[0])
            if isZeroes:
                break
        nextValue = part2values[-1]
        for i in range(len(part2values)):
            nextValue = part2values[-i-1] - nextValue
        part2totalValue += nextValue
        part1totalValue += part1value
    print("PART 1: " + str(part1totalValue))
    print("PART 2: " + str(part2totalValue))


def createNumberedList(file):
    numlist = []
    for line in file:
        charArr = line.split()
        numArr = []
        for i in range(len(charArr)):
            numArr.append(int(charArr[i]))
        numlist.append(numArr)
    return numlist


def getNextSeq(seq):
    nextSeq = []
    zeroCount = 0
    for i in range(len(seq)-1):
        nextSeq.append(seq[i+1]-seq[i])
        if seq[i+1]-seq[i] == 0:
            zeroCount += 1
    if zeroCount == len(nextSeq):
        return nextSeq, True
    else:
        return nextSeq, False
    

main()