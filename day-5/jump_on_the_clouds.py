def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    n = len(c)

    while True:
        energy = energy - 1 - (2 *c[i])
        i = (i + k) % n
        if i == 0:
            break

    return energy

if __name__ == '__main__':

    k = int(input("Enter the size of Jump on cloud: "))

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)