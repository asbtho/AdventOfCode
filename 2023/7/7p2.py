import functools
def main():
    file = open(0).read().splitlines()

    hands = {}

    five = []
    four = []
    full = []
    three = []
    twopair = []
    onepair = []
    high = []
    rank = []
    
    for line in file:
        hand = line.split()
        hands[hand[0]] = hand[1]

    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    for h, hand in enumerate(hands):
        thisWasAdded = False
        if not thisWasAdded:
            for x, c in enumerate(hand):
                if hand.count(hand[0]) == 5:
                    five.append(hand)
                    thisWasAdded = True
                    break
                elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
                    isAdded = False
                    if hand.count("J") == 4 or hand.count("J") == 1:
                        five.append(hand)
                        thisWasAdded = True
                        isAdded = True
                        break
                    if isAdded:
                        break
                    else:
                        four.append(hand)
                        thisWasAdded = True
                        break
                elif hand.count(hand[x]) == 3:
                    isAdded = False
                    if hand.count("J") == 3 or hand.count("J") == 2:
                         for card in cards:
                            if card != "J" and (hand.count(card) == 2 or hand.count(card) == 3):
                                five.append(hand)
                                thisWasAdded = True
                                isAdded = True
                                break
                    if isAdded:
                        break
                    else:
                        if hand.count("J") == 1:
                            for card in cards:
                                if card != "J" and hand.count(card) == 3:
                                    four.append(hand)
                                    thisWasAdded = True
                                    isAdded = True
                                    break
                    if isAdded:
                        break
                    else:
                        for card in cards:
                            if card != hand[x] and hand.count(card) == 2:
                                full.append(hand)
                                thisWasAdded = True
                                isAdded = True
                                break
                    if isAdded:
                        break
                    else:
                        if hand.count("J") == 2:
                            continue
                        else:
                            three.append(hand)
                            thisWasAdded = True
                            break
                elif hand.count(hand[x]) == 2:
                    isAdded = False
                    if hand.count("J") == 3:
                         for card in cards:
                            if card != "J" and hand.count(card) == 2:
                                five.append(hand)
                                thisWasAdded = True
                                isAdded = True
                                break
                    if isAdded:
                        break
                    else:
                        if hand.count("J") == 2:
                            for card in cards:
                                if card != "J" and hand.count(card) == 3:
                                    five.append(hand)
                                    thisWasAdded = True
                                    isAdded = True
                                    break
                                if card != "J" and hand.count(card) == 2:
                                    four.append(hand)
                                    thisWasAdded = True
                                    isAdded = True
                                    break
                            if isAdded:
                                break
                            else:
                                three.append(hand)
                                thisWasAdded = True
                                isAdded = True
                                break
                    if isAdded:
                        break
                    else:
                        if hand.count("J") == 1:
                            for card in cards:
                                if card != "J" and card != hand[x] and hand.count(card) == 2:
                                    full.append(hand)
                                    thisWasAdded = True
                                    isAdded = True
                                    break
                    if isAdded:
                        break
                    else:
                        if hand.count("J") == 1:
                            for card in cards:
                                if card != "J" and hand.count(card) == 2:
                                    three.append(hand)
                                    thisWasAdded = True
                                    isAdded = True
                                    break
                    if isAdded:
                        break
                    else:
                        for card in cards:
                            if card != hand[x] and hand.count(card) == 2 and hand.count(card) != 3 and hand.count(hand[x]) != 3:
                                twopair.append(hand)
                                thisWasAdded = True
                                isAdded = True
                                break
                            if card != hand[x] and hand.count(card) == 3:
                                full.append(hand)
                                thisWasAdded = True
                                isAdded = True
                                break
                    if isAdded:
                        break
                    else:
                        onepair.append(hand)
                        thisWasAdded = True
                        break
                else:
                    continue
        if(thisWasAdded):
            continue
        else:
            if hand.count("J") == 1:
                onepair.append(hand)
            else:
                high.append(hand)

    sorthigh = sorted(high, key=functools.cmp_to_key(compare))
    sortonepair = sorted(onepair, key=functools.cmp_to_key(compare))
    sorttwopair = sorted(twopair, key=functools.cmp_to_key(compare))
    sortthree = sorted(three, key=functools.cmp_to_key(compare))
    sortfull = sorted(full, key=functools.cmp_to_key(compare))
    sortfour = sorted(four, key=functools.cmp_to_key(compare))
    sortfive = sorted(five, key=functools.cmp_to_key(compare))

    for c in sortonepair:
        print(c)

    for hand in sortfive:
        rank.append(hand)
    for hand in sortfour:
        rank.append(hand)
    for hand in sortfull:
        rank.append(hand)
    for hand in sortthree:
        rank.append(hand)
    for hand in sorttwopair:
        rank.append(hand)
    for hand in sortonepair:
        rank.append(hand)
    for hand in sorthigh:
        rank.append(hand)

    totalWinnings = 0
    for x, hand in enumerate(rank):
        rankNumber = len(hands)-x
        winnings = int(hands[hand]) * rankNumber
        #print("HAND: " + hand + " WINNINGS: " + str(winnings) + " BID: " + hands[hand])
        totalWinnings += winnings
    
    print("TOTAL WINNINGS: " + str(totalWinnings))

def compare(hand1, hand2):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    for x in range(6):
        if cards.index(hand1[x]) < cards.index(hand2[x]):
            return -1
        if cards.index(hand1[x]) > cards.index(hand2[x]):
            return 1
    return 0

main()