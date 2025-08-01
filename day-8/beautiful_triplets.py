def beautifulTriplets(d, arr):
    count = 0
    set_arr = set(arr)
    
    for num in arr:
        if (num + d) in set_arr and (num + 2*d) in set_arr:
            count += 1
    
    return count

if __name__ == '__main__':

    d = int(input("Enter the number to compare: "))

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)