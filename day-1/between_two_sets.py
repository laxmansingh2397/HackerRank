import math
arr = [2, 4]
brr = [16, 32, 96]

def getTotalX(arr, brr):
    result = 0
    lcm = math.lcm(*arr)
    gcd = math.gcd(*brr)
    multiple = 0

    while multiple <= gcd:
        multiple += lcm

        if (gcd % multiple == 0):
            result += 1
    
    return result


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)