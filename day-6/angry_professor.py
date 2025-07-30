

def angryProfessor(k, a):
    count_arrived = 0

    for i in a:
        if i <= 0:
            count_arrived += 1
    print(count_arrived)
    if count_arrived >= k:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':

    k = int(input("Enter the threshold: "))

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)

    print(result)
