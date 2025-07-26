# UDDDUDUU

def countingValleys(steps, path):
    
    valley_count = 0
    level = 0

    dic = {"U":1, "D": -1}

    for step in path:
        level += dic[step]
        if level == 0 and step == "U":
            valley_count += 1
            
    
    return valley_count


if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
