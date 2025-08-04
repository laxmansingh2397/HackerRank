# n=5


def utopianTree(n):
    height = []

    if n < 1:
        return 1


    for i in range(n):

        if i < 1:
            height.append(1)
        
        if i % 2 == 1:
            print(height[-1])
            height.append(height[-1] + 1)
        if i % 2 == 0:
            print(height[-1])
            height.append(height[-1] * 2)
    print(height)
    return height[n]


if __name__ == '__main__':

    n = int(input().strip())

    result = utopianTree(n)

    print(result)
