

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)

    for number in arr:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1
    
    return f"{positive/n:6f}\n{negative/n:6f}\n{zero/n:6f}"


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)

    print(result)