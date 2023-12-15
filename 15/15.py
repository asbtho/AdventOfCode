def main():
    seq, sum = open(0).read().strip().split(","),0
    for step in seq:
        sum += hashAlgorithm(step,0)
    print(sum)
    
def hashAlgorithm(string,value):
    for char in string:
        value = ((value + ord(char))*17) % 256
    return value

main()