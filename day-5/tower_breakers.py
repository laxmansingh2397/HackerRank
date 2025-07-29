


def towerBreakers(n, m):
    
    height = m
    number_of_towers = n

    if height == 1 or number_of_towers % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':

    n = int(input("Enter number: "))

    m = int(input("Enter number: "))

    result = towerBreakers(n, m)

    print(result)
