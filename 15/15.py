def main():
    seq, sum = open(0).read().strip().split(","),0
    #part1(seq,sum)
    part2(seq)
    
def hashAlgorithm(string,value):
    for char in string:
        value = ((value + ord(char))*17) % 256
    return value

def getOperationAndLabel(string):
    if string[-1].isdigit():
        operation,focal,label = string[-2],string[-1],string[:-2]
    else:
        operation,focal,label = string[-1],-1,string[:-1]
    return operation,focal,label

def part1(seq,sum):
    for step in seq:
        sum += hashAlgorithm(step,0)
    print(sum)

def part2(seq):
    boxes = createBoxes()
    for string in seq:
        operation,focal,label = getOperationAndLabel(string)
        box = hashAlgorithm(label,0)
        if operation == "-":
            boxes[box] = removeLabel(label,boxes[box])
        else:
            boxes[box] = addLabel(label,focal,boxes[box])
    calculateFocusPower(boxes,0)

def createBoxes():
    boxes = {}
    for i in range(255):
        boxes[i] = []
    return boxes

def removeLabel(label,box):
    for entry in box:
        if label in entry:
            box.remove(entry)
    return box

def addLabel(label,focal,box):
    for i, entry in enumerate(box):
        if label in entry:
            box[i] = label + " " + focal
            return box
    box.append(label + " " + focal)
    return box

def calculateFocusPower(boxes,value):
    for boxNumber,box in boxes.items():
        value += boxFocusPower(box,boxNumber,0)
    print(value)

def boxFocusPower(box,boxNumber,value):
    for i, entry in enumerate(box):
        value += (1+boxNumber)*(i+1)*int(entry[-1])
    return value


main()