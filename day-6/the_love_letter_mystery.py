def theLoveLetterMystery(s):
    reverse = s[::-1]
    count = 0
    for i in range(len(s)):
        count += abs(ord(s[i]) - ord(reverse[i]))

    return count // 2


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)