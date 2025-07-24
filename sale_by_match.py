# n = 7
# arr = [1,2,1,2,1,3,2]


def sockMerchant(n, ar):
    count = 0
    arr_set = set(ar)

    for i in arr_set:
        number = ar.count(i)
        number = number // 2
        count += number
    return count



if __name__ == "__main__":
    
    n = int(input("Enter array length: ").strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)