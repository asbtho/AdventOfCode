### Solution followed HyperNeutrino's solution for learning.

def main():
    lines = open(0)
    
    total = 0
    
    for line in lines:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))

        cfg = "?".join([cfg] * 5)
        nums *= 5

        total += count(cfg, nums)

    print(total)


cache = {}
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in cfg else 1
    
    key = (cfg, nums)

    if key in cache:
        return cache[key]
    
    result = 0

    if cfg[0] in ".?":
        #print("CFG in '.?' : " + cfg)
        result += count(cfg[1:],nums)
        #print(result)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            #print("CFG in '#?' : " + cfg)
            result += count(cfg[nums[0] + 1:], nums[1:])
            #print(result)

    cache[key] = result
    return result


main()
