# arr =3 -7 0

def minimumAbsoluteDifference(arr):
    arr.sort()

    min_diff = float('inf')

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff

    return min_diff

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)