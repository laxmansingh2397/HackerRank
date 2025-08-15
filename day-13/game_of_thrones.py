def gameOfThrones(s):
    s_dict = {}
    for i in s:
        s_dict[i] = s_dict.get(i,0)+1

    odd = 0
    for i in s_dict.values():
        if i % 2 == 1:
            odd += 1

    return "YES" if odd <= 1 else "NO"

if __name__ == '__main__':

    s = input()

    result = gameOfThrones(s)

    print(result)
    