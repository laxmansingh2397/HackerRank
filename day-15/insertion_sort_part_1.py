def insertionSort1(n, arr):
    nums = arr[-1]
    for i in range(len(arr)-1,0,-1):
        if nums < arr[i-1]:
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = nums
            print(*arr)
            break
    else:
        arr[0] = nums
        print(*arr)

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(insertionSort1(n, arr))
