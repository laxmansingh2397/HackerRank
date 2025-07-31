

def lonelyinteger(a):
    
    lonely_integer = 0
    set_a = set(a)

    if len(a) < 2:
        return a[0]

    for i in set_a:
        if a.count(i) == 1:
            lonely_integer = i
    
    return lonely_integer


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)