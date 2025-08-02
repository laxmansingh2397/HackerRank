def maxMin(k, arr):
    arr.sort()
    min_diff = sys.maxsize

    for i in range(len(arr)-k+1):
        min_diff = min(min_diff, arr[i+k-1] - arr[i])
    
    return min_diff
    



if __name__ == '__main__':

    k = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maxMin(k, arr)

    print(result)
