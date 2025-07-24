
a = [5, 6, 7]
b = [3, 6, 10]

def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] == b[i]:
            continue
        else:
            bob += 1

    return alice, bob



if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)