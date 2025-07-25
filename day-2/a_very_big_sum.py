


def aVeryBigSum(ar):
    sum = 0

    for number in ar:
        sum += number

    return sum

if __name__ == '__main__':

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)