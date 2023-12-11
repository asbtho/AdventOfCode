import time
def main():
    file = open(0).read().splitlines()
    part1(file)
    part2(file)


# PART 1
def part1(file):
    total = 0
    for line in file:
        points = 0
        card, numbers = line.split(": ",1)
        winning, my = numbers.split(" | ",1)
        winning = winning.split(" ")
        my = my.split(" ")
        firstPoint = True
        for i, wincard in enumerate(winning):
            if wincard == "":
                continue
            if wincard in my:
                if firstPoint:
                    points += 1
                    firstPoint = False
                else:
                    points *= 2
        #print(card + ": " + str(points))
        total += points
    print("PART 1: " + str(total))


# PART 2
def part2(file):
    startTime = time.time()
    total = 0
    card_list = {}

    for x, line in enumerate(file):
        card = line.split(": ",1)[0]
        card = card.replace("   "," ")
        card = card.replace("  "," ")
        #print(card)
        card_list[card] = 1

    for x, line in enumerate(file):
        #print("Iteration: " + str(x+1))
        card, numbers = line.split(": ",1)
        card = card.replace("   "," ")
        card = card.replace("  "," ")
        winning, my = numbers.split(" | ",1)
        winning = winning.split(" ")
        my = my.split(" ")
        
        for i in range(card_list[card]):
            match = 0

            for y, wincard in enumerate(winning):
                if wincard == "":
                    continue
                if wincard in my:
                    # Add Copies
                    nextCard = "Card "+ str((x+2+match))
                    card_list[nextCard] += 1
                    match += 1
    
    for card in card_list:
        total += card_list[card]
    executionTime = (time.time() - startTime)
    #print(card_list)
    print("PART 2: " +str(total))
    print('PART 2 Execution time in seconds: ' + str(executionTime))



main()