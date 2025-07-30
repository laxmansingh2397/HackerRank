def equalizeArray(arr):
    same_max_number_count = 0
    count_number = 0
    unique_arr = set(arr)
    for i in unique_arr:
        count = arr.count(i)
        same_max_number_count= max(same_max_number_count,count)
        if count == same_max_number_count:
            count_number = i

    delete_number = 0
    for i in arr:
        if i != count_number:
            delete_number += 1

    return delete_number


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)