def happyLadybugs(b):
    if "_" not in b:
        n = len(b)
        for i in range(n):
            left_same = (i > 0 and b[i] == b[i-1])
            right_same = (i < n - 1 and b[i] == b[i+1])
            if not (left_same or right_same):
                return "NO"
        return "YES"

    for ch in set(b):
        if ch != "_" and b.count(ch) == 1:
            return "NO"
    return "YES"

if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        print(result)
