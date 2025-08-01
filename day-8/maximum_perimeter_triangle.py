def maximumPerimeterTriangle(sticks):
    sticks.sort()
    i = len(sticks) - 3

    while i >=0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
        i -= 1

    if i >= 0:
        return [sticks[i], sticks[i+1], sticks[i+2]]
    else:
        return -1
    


if __name__ == '__main__':

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(result)