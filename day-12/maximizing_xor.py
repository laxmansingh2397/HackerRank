def maximizingXor(l, r):
    max_sum = 0
    for i in range(l,r+1):
        for j in range(l, r+1):
            xor = i^j
            max_sum = max(xor,max_sum)
    return max_sum

if __name__ == '__main__':

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    print(result)
