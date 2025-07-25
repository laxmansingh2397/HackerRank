# s =1 2 1 3 2
# d =3 
# m = 2

def birthday(s, d, m):
    count = 0
    i = 0
    j = m

    while j <= len(s):
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    return count



if __name__ == '__main__':


    s = list(map(int, input().rstrip().split()))

    

    d = int(input("Enter the birth day: "))

    m = int(input("Enter the birth month: "))

    result = birthday(s, d, m)

    print(result)