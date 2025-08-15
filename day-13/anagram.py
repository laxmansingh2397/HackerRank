def anagram(s):
    s1 = list(s[:len(s)//2])
    s2 = list(s[len(s)//2:])

    if len(s) % 2 == 1:
        return -1

    for i in s1:
        for j in s2:
            if i == j:
                s2.remove(j)
                break
    return len(s2)


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
