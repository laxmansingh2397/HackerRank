def cutTheSticks(arr):
    new_arr = []

    while len(arr) != 0:
        min_length = min(arr)
        new_arr.append(len(arr))
        arr = [num for num in arr if num != min_length]

    return new_arr

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print(result)
