# p = 5 2 1 3 4

def permutationEquation(p):
    
    new_p = []

    for i in range(1, len(p) + 1):
        x = p.index(i) + 1
        print(x)
        y = p.index(x) + 1
        new_p.append(y)

    return new_p


if __name__ == '__main__':

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)