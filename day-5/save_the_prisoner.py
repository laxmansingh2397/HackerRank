def saveThePrisoner(n, m, s):
    
    return (s - 1 + m - 1) % n + 1


if __name__ == '__main__':
    n = int(input("Enter the number of prisoner: "))

    m = int(input("Enter the number of candy: "))

    s = int(input("Enter the postion where to start: "))

    result = saveThePrisoner(n, m, s)

    print(result)
