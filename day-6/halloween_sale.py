
def howManyGames(p, d, m, s):
    count = 0
    budget = s
    price = p
    while budget >= price:
        budget -= price
        count += 1
        price = max(price - d, m)

    return count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
