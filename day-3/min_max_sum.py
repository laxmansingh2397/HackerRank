# arr = 1 2 3 4 5

def miniMaxSum(arr):

    arr.sort()

    min_sum = sum(arr) - arr[-1]
    max_sum = sum(arr) - arr[0]   

    return min_sum,max_sum

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = miniMaxSum(arr)

    print(result)