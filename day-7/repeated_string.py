

def repeatedString(s, n):
    
    count_a_in_s = s.count("a")

    full_repeate = n // len(s)

    remainder = n % len(s)

    count_a_in_remainder = s[:remainder].count("a")

    return full_repeate * count_a_in_s + count_a_in_remainder

if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)