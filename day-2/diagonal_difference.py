# arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]



def diagonalDifference(arr):
    n = len(arr)
    left_diagonal = 0
    right_diagonal = 0

    for i in range(len(arr)):
        left_diagonal += arr[i][i]
        right_diagonal += arr[n-1-i][i]

    return abs(left_diagonal - right_diagonal)



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
