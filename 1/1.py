def main():
    mydict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    file = open('input.txt','r')
    sum = 0
    for line in file:
        sum += int(getNumber(line,mydict))
    return sum

def getNumber(line,mydict):
    number = ""
    n = -1
    for i in line:
        n += 1
        threeString = line[n:n+3]
        fourString = line[n:n+4]
        fiveString = line[n:n+5]
        if i.isdigit():
            number += i
            break
        elif threeString in mydict:
            number += mydict.get(threeString)
            break
        elif fourString in mydict:
            number += mydict.get(fourString)
            break
        elif fiveString in mydict:
            number += mydict.get(fiveString)
            break

    n = len(line)
    for i in reversed(line):
        n -= 1
        threeString = line[n-3:n]
        fourString = line[n-4:n]
        fiveString = line[n-5:n]
        if i.isdigit():
            number += i
            break
        elif threeString in mydict:
            number += mydict.get(threeString)
            break
        elif fourString in mydict:
            number += mydict.get(fourString)
            break
        elif fiveString in mydict:
            number += mydict.get(fiveString)
            break
    
    return number


print(main())