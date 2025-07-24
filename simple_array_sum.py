
n = 6
ar = [1,2,3,4,10,11]


def simpleArraySum(ar):
    count = 0

    for i in ar:
        count += i
    
    return count



if __name__ == "__main__":

    n = int(input("Enter array length: ").strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)